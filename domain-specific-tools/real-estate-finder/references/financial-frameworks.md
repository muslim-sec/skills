# Financial Frameworks Reference

كل المعادلات والقواعد المالية المستخدمة في الـ Real Estate Finder Dashboard.

---

## 1. Affordability — قاعدة 28/36

### الأصل:
- **الـ Housing Cost Ratio** (نسبة الإسكان من الدخل): max 28% من الدخل الإجمالي الشهري
- **الـ Total Debt Ratio** (نسبة الدين الكلي): max 36% من الدخل الإجمالي الشهري

### الاستخدام:
```javascript
// Max safe monthly housing payment
const maxMonthlyHousing = grossMonthlyIncome * 0.28;

// Max total monthly debt (housing + other obligations)
const maxTotalDebt = grossMonthlyIncome * 0.36;

// Available for housing AFTER existing obligations
const availableForHousing = Math.min(
  maxMonthlyHousing,
  maxTotalDebt - existingMonthlyObligations
);
```

### Health Indicators:
| Housing-to-Income Ratio | Status | Color |
|------------------------|--------|-------|
| < 25% | ممتاز — مساحة أمان كبيرة | 🟢 أخضر |
| 25-33% | مقبول — في الحد المسموح | 🟡 أصفر |
| > 33% | خطر — الـ housing هياكل من راحتك المالية | 🔴 أحمر |

### ملاحظة إقليمية:
البنوك في مصر بتطلب نسبة Debt-to-Income أقل من 35-50% (يختلف من بنك لتاني). البنوك السعودية بتسمح حتى 65% للوظائف الحكومية، 55% للقطاع الخاص. الإمارات حد 50%.

---

## 2. Mortgage Payment Formula

### المعادلة الأساسية (Amortization):
```
M = P × [r(1+r)^n] / [(1+r)^n - 1]
```
- M = القسط الشهري
- P = أصل القرض (Principal)
- r = نسبة الفائدة الشهرية (annual rate / 12 / 100)
- n = عدد الأشهر (years × 12)

### الكود:
```javascript
function monthlyMortgagePayment(principal, annualRatePercent, years) {
  if (principal <= 0 || years <= 0) return 0;
  if (annualRatePercent === 0) return principal / (years * 12);
  
  const r = annualRatePercent / 12 / 100;
  const n = years * 12;
  const factor = Math.pow(1 + r, n);
  return principal * (r * factor) / (factor - 1);
}
```

### Reverse: حساب أقصى سعر عقار من قسط متاح
```javascript
function maxPropertyPrice(maxMonthlyPayment, annualRatePercent, years, downPaymentPercent) {
  if (maxMonthlyPayment <= 0) return 0;
  const r = annualRatePercent / 12 / 100;
  const n = years * 12;
  
  // Max loan amount the user can take
  let maxLoan;
  if (r === 0) {
    maxLoan = maxMonthlyPayment * n;
  } else {
    const factor = Math.pow(1 + r, n);
    maxLoan = maxMonthlyPayment * (factor - 1) / (r * factor);
  }
  
  // Down payment % means loan covers (100 - down)%
  // So total price = maxLoan / (1 - downPayment/100)
  return maxLoan / (1 - downPaymentPercent / 100);
}
```

### Total Interest Paid:
```javascript
function totalInterest(principal, annualRatePercent, years) {
  const monthly = monthlyMortgagePayment(principal, annualRatePercent, years);
  return (monthly * years * 12) - principal;
}
```

---

## 3. Investment ROI Metrics

### Gross Rental Yield (العائد الإجمالي)
```
Gross Yield (%) = (Annual Rent / Property Price) × 100
```
```javascript
const grossYield = (monthlyRent * 12 / propertyPrice) * 100;
```

### Net Rental Yield (العائد الصافي) — الأهم
```
Net Yield (%) = ((Annual Rent - Annual Operating Expenses) / Property Price) × 100
```
Operating expenses include: maintenance, management, taxes, insurance, vacancy loss
```javascript
const effectiveRent = monthlyRent * 12 * (occupancyRate / 100);
const annualExpenses = maintenancePercent / 100 * propertyPrice 
                     + managementPercent / 100 * effectiveRent
                     + annualTaxes;
const netYield = ((effectiveRent - annualExpenses) / propertyPrice) * 100;
```

### Cash-on-Cash Return (مهم لو فيه قرض)
```
Cash-on-Cash (%) = (Annual Cash Flow / Total Cash Invested) × 100
```
```javascript
const annualMortgage = monthlyPayment * 12;
const annualCashFlow = effectiveRent - annualExpenses - annualMortgage;
const totalCashInvested = downPayment + closingCosts;
const cashOnCash = (annualCashFlow / totalCashInvested) * 100;
```

### Cap Rate (Capitalization Rate)
```
Cap Rate (%) = NOI / Property Price × 100
```
حيث NOI = Net Operating Income (الإيجار - المصاريف، **بدون** القرض)
```javascript
const NOI = effectiveRent - annualExpenses;
const capRate = (NOI / propertyPrice) * 100;
```

### Break-even (نقطة التعادل)
```javascript
// كم شهر علشان الـ cash flow يغطي الـ down payment
function breakEvenMonths(downPayment, monthlyCashFlow) {
  if (monthlyCashFlow <= 0) return Infinity;
  return Math.ceil(downPayment / monthlyCashFlow);
}
```

### Total Return Projection (5/10/15 years)
```javascript
function projectTotalReturn(
  propertyPrice, downPayment, monthlyRent, expenses,
  appreciationRatePercent, holdingYears, monthlyMortgage
) {
  const projection = [];
  let currentValue = propertyPrice;
  let cumulativeCashFlow = 0;
  
  for (let year = 1; year <= holdingYears; year++) {
    currentValue *= (1 + appreciationRatePercent / 100);
    const annualCashFlow = (monthlyRent * 12) - expenses - (monthlyMortgage * 12);
    cumulativeCashFlow += annualCashFlow;
    
    const equity = currentValue - propertyPrice + downPayment; // simplified
    const totalReturn = cumulativeCashFlow + (currentValue - propertyPrice);
    
    projection.push({ year, currentValue, cumulativeCashFlow, totalReturn });
  }
  return projection;
}
```

---

## 4. Rent vs Buy Calculator

### الأصل: مقارنة الـ wealth بعد X سنين في السيناريوهين

#### سيناريو الإيجار:
- لكل شهر: يدفع إيجار + يدخر الفرق (لو الشراء كان أغلى) + يدخر الـ down payment المتاح
- المدخرات تتراكم بفائدة سنوية معقولة (default 5% في الخليج، 12-15% في مصر)

```javascript
function rentScenario(monthlyRent, monthlyAlternativeCost, downPaymentCash, years, savingsRatePercent) {
  const monthlyDiff = Math.max(0, monthlyAlternativeCost - monthlyRent);
  let savings = downPaymentCash;
  const months = years * 12;
  const monthlyReturn = savingsRatePercent / 12 / 100;
  
  for (let m = 0; m < months; m++) {
    savings = savings * (1 + monthlyReturn) + monthlyDiff;
  }
  return savings;
}
```

#### سيناريو الشراء:
- يدفع الـ down payment upfront
- يدفع قسط شهري + صيانة + رسوم
- بعد X سنين: قيمة العقار - الباقي من القرض = الـ equity
- + إيجار افتراضي (لو يأجره) لو investment

```javascript
function buyScenario(propertyPrice, downPayment, mortgageRate, loanYears, holdingYears, appreciationRate) {
  const loanAmount = propertyPrice - downPayment;
  const monthly = monthlyMortgagePayment(loanAmount, mortgageRate, loanYears);
  
  // Property value after holding years
  const futureValue = propertyPrice * Math.pow(1 + appreciationRate / 100, holdingYears);
  
  // Remaining loan balance
  const monthsPaid = holdingYears * 12;
  const r = mortgageRate / 12 / 100;
  const n = loanYears * 12;
  const remainingBalance = loanAmount * 
    (Math.pow(1 + r, n) - Math.pow(1 + r, monthsPaid)) / 
    (Math.pow(1 + r, n) - 1);
  
  return {
    futureValue,
    remainingBalance,
    equity: futureValue - remainingBalance,
    totalPaid: monthly * monthsPaid + downPayment
  };
}
```

#### Break-even Point:
ابحث عن السنة اللي فيها `buyEquity > rentSavings` لأول مرة.

---

## 5. Islamic Financing (تمويل إسلامي) — المرابحة

### الفرق عن القرض التقليدي:
- البنك يشتري العقار ويبيعه للعميل بربح متفق عليه
- القسط ثابت طول مدة العقد (بدون فائدة متغيرة)
- الربح الإجمالي محدد من الأول

### الحساب:
```javascript
function murabahaPayment(propertyPrice, downPayment, profitRatePercent, years) {
  const principal = propertyPrice - downPayment;
  // البنك يضيف الربح الكلي على الأصل ويقسم على عدد الأشهر
  const totalProfit = principal * (profitRatePercent / 100) * years;
  const totalAmount = principal + totalProfit;
  return totalAmount / (years * 12);
}
```

في الـ dashboard، اعرض toggle بين Conventional و Islamic، الـ Islamic عادة أعلى قليلاً في الـ effective rate لكن أبسط وثابت.

---

## 6. Total Cost of Ownership (TCO) Calculator

علشان نديله صورة كاملة عن التكلفة الحقيقية، ضع في الحسبان:

### Upfront Costs:
- Down Payment
- **Registration fees** — مصر ~2.5%، السعودية VAT 5% للجديد، الإمارات 4% DLD
- **Broker fees** — عادة 2-3%
- **Legal fees** — ~1%
- **Initial maintenance/furnishing** — حسب الحالة

### Recurring Costs:
- Monthly mortgage/rent payment
- **Property maintenance** — عادة 1% سنوياً من قيمة العقار
- **Service charges** (compound, building) — مهم في الخليج خاصة
- **Property tax** — حسب الدولة (مصر: ضريبة عقارية إذا قيمة > 2 مليون جنيه)
- **Insurance** — اختياري لكن مهم

### الكود:
```javascript
function totalCostOfOwnership(price, downPaymentPercent, country, years) {
  const data = REGIONAL_DATA[country];
  const downPayment = price * downPaymentPercent / 100;
  const registrationFees = price * data.registrationFeePercent / 100;
  const brokerFees = price * 0.025;
  const legalFees = price * 0.01;
  
  const upfrontTotal = downPayment + registrationFees + brokerFees + legalFees;
  
  const annualMaintenance = price * 0.01;
  const annualServiceFees = data.avgServiceFees; // fixed for property type
  const annualPropertyTax = price > data.taxThreshold ? price * data.taxRate / 100 : 0;
  
  const recurringTotal = (annualMaintenance + annualServiceFees + annualPropertyTax) * years;
  
  return { upfrontTotal, recurringTotal, grandTotal: upfrontTotal + recurringTotal };
}
```

---

## 7. Recommendation Scoring Algorithm

علشان نقدر نطلع توصية ذكية في Tab 6، احسب score من 0-100 على عدة محاور:

```javascript
function calculateRecommendationScore(profile, financials, defaults) {
  let score = 50; // start neutral
  const reasons = [];
  const risks = [];
  
  // Affordability check (40 points)
  const housingRatio = (estimatedMonthlyCost / financials.monthlyIncome) * 100;
  if (housingRatio < 25) { score += 20; reasons.push('السكن مريح من ناحية النسبة من الدخل'); }
  else if (housingRatio < 33) { score += 10; reasons.push('السكن في الحد المقبول'); }
  else { score -= 20; risks.push(`نسبة السكن من الدخل (${housingRatio.toFixed(1)}%) أعلى من المسموح`); }
  
  // Down payment readiness (20 points)
  if (financials.savings >= requiredDownPayment * 1.2) { score += 20; reasons.push('عندك سيولة كافية + هامش أمان'); }
  else if (financials.savings >= requiredDownPayment) { score += 10; }
  else { score -= 15; risks.push('السيولة المتاحة أقل من الـ down payment المطلوب'); }
  
  // Investment fit (if applicable)
  if (profile.goal.includes('investment')) {
    if (netYield >= defaults.avgRentalYield) { score += 15; reasons.push(`الـ yield (${netYield.toFixed(1)}%) فوق متوسط المنطقة`); }
    else { score -= 10; risks.push(`الـ yield تحت متوسط المنطقة`); }
  }
  
  // Timing
  if (profile.timeline === 'immediate' && financials.savings < requiredDownPayment) {
    score -= 15;
    risks.push('العجلة في القرار مع نقص السيولة = خطر');
  }
  
  // Final recommendation
  let recommendation;
  if (score >= 75) recommendation = 'GO — اشتري بثقة';
  else if (score >= 55) recommendation = 'PROCEED WITH CAUTION — اشتري مع مراعاة الـ risks';
  else if (score >= 35) recommendation = 'WAIT — حسّن وضعك المالي شوية الأول';
  else recommendation = 'DO NOT BUY NOW — أجّر/استنى';
  
  return { score, recommendation, reasons, risks };
}
```

---

## 8. Currency Inflation Hedge (مهم لمصر تحديداً)

في الاقتصادات اللي بتعاني من تضخم/تقلب عملة (مصر مثلاً)، العقار عادة hedge كويس. لكن **القرض بالعملة المحلية** ميزة لأن قيمته بتقل مع التضخم.

في الـ Dashboard، أضف قسم optional:
```
"لو افترضنا تضخم سنوي X% للعملة، القيمة الحقيقية للقسط بعد 5 سنين هتقل بنسبة Y%"
```

```javascript
function realValueAfterInflation(nominalAmount, inflationRatePercent, years) {
  return nominalAmount / Math.pow(1 + inflationRatePercent / 100, years);
}
```
