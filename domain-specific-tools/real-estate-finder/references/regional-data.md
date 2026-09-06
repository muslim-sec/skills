# Regional Data Reference — Middle East Real Estate

أرقام مرجعية لاستخدامها كـ default values في الـ Dashboard. **الأرقام دي تقريبية ومرجعية فقط** — لازم المستخدم يتحقق منها مع جهات رسمية قبل أي قرار.

> ⚠️ Note for Claude: الأرقام دي قد تكون قديمة. **قبل ما تعتمد عليها في dashboard للمستخدم، حاول تتحقق من Exa MCP لو متاح** (راجع Phase 0.5 في SKILL.md):
> - `tool_search(query="exa web search")` للتأكد من توفر Exa
> - `Exa:web_search_exa({ query: "current [city] real estate prices [year]" })` لتحديث الأسعار
> - `Exa:web_search_exa({ query: "[country] mortgage rates [current year]" })` لتحديث نسب الفائدة
>
> لو Exa مش متاح، استخدم `web_search` العادي. الـ defaults دي معقولة كـ starting point لكن السوق بيتحرك.

---

## REGIONAL_DATA Object — استخدمها في الـ artifact

```javascript
const REGIONAL_DATA = {
  egypt: {
    name: 'مصر',
    nameEn: 'Egypt',
    currency: 'EGP',
    currencySymbol: 'ج.م',
    locale: 'ar-EG',
    mortgageRate: 22,           // % conventional, varies 18-26%
    islamicProfitRate: 24,      // % murabaha approx
    downPaymentMin: 30,         // % typically 25-50%
    loanTenureMax: 20,          // years (CBE initiative allows up to 30 for low-income)
    avgRentalYield: 7,          // % gross
    propertyAppreciation: 15,   // % annual nominal (high due to inflation)
    inflationRate: 25,          // % approx
    registrationFeePercent: 2.5,
    avgServiceFees: 6000,       // EGP/year typical mid-range compound
    taxThreshold: 2000000,      // EGP — above this, property tax applies
    taxRate: 0.001,             // 10% of rental value, capped
    popularAreas: [
      'القاهرة الجديدة', 'الشيخ زايد', '6 أكتوبر', 'العاصمة الإدارية',
      'الساحل الشمالي', 'العين السخنة', 'المعادي', 'الزمالك',
      'مدينة نصر', 'مصر الجديدة', 'الإسكندرية'
    ],
    notes: 'تقلب العملة عامل خطر كبير. عقارات Compounds في القاهرة الجديدة والشيخ زايد هي الأكثر استقراراً.',
  },
  
  saudi: {
    name: 'السعودية',
    nameEn: 'Saudi Arabia',
    currency: 'SAR',
    currencySymbol: 'ر.س',
    locale: 'ar-SA',
    mortgageRate: 7,            // % SAIBOR + margin
    islamicProfitRate: 7.5,
    downPaymentMin: 10,         // % REDF/Sakani schemes allow lower
    loanTenureMax: 30,
    avgRentalYield: 6,
    propertyAppreciation: 4,
    inflationRate: 2.5,
    registrationFeePercent: 0,  // No registration fee for primary residence
    realEstateVAT: 5,           // % for new properties (first sale)
    avgServiceFees: 8000,       // SAR/year
    taxThreshold: 999999999,    // No property tax for individuals
    taxRate: 0,
    popularAreas: [
      'الرياض الشمالية', 'الياسمين', 'الملقا', 'الواحة',
      'حي السفارات', 'حي الورود', 'جدة - أبحر',
      'الخبر - العقربية', 'الدمام'
    ],
    notes: 'برنامج سكني (REDF) بيدعم المواطنين بتمويل ميسر. السوق مستقر نسبياً، الـ off-plan شائع.',
  },
  
  uae: {
    name: 'الإمارات',
    nameEn: 'UAE',
    currency: 'AED',
    currencySymbol: 'د.إ',
    locale: 'ar-AE',
    mortgageRate: 4.5,          // % varies 3.5-5.5%
    islamicProfitRate: 5,
    downPaymentMin: 20,         // % expats 25%, citizens 15%, off-plan 50%
    loanTenureMax: 25,
    avgRentalYield: 6.5,
    propertyAppreciation: 5,
    inflationRate: 3,
    registrationFeePercent: 4,  // DLD fee
    avgServiceFees: 12000,      // AED/year for mid-range
    taxThreshold: 999999999,    // No property tax
    taxRate: 0,
    popularAreas: [
      'دبي مارينا', 'داون تاون دبي', 'JVC', 'Business Bay',
      'Dubai Hills', 'Palm Jumeirah', 'JBR', 'Damac Hills',
      'أبو ظبي - الريم', 'ياس آيلاند', 'الشارقة - الخان'
    ],
    notes: 'دبي/أبو ظبي بيسمحوا للأجانب يتملكوا في freehold areas. Off-plan شائع جداً مع payment plans. DLD fees مهم في الحسبة.',
  },
  
  qatar: {
    name: 'قطر',
    nameEn: 'Qatar',
    currency: 'QAR',
    currencySymbol: 'ر.ق',
    locale: 'ar-QA',
    mortgageRate: 5.5,
    islamicProfitRate: 6,
    downPaymentMin: 20,
    loanTenureMax: 25,
    avgRentalYield: 6,
    propertyAppreciation: 3,
    inflationRate: 3,
    registrationFeePercent: 0.25,
    avgServiceFees: 10000,
    taxThreshold: 999999999,
    taxRate: 0,
    popularAreas: ['الدوحة - اللؤلؤة', 'لوسيل', 'الوسيل', 'الخليج الغربي', 'المعراض'],
    notes: 'السوق هادي ومركزة في الدوحة. القانون بيسمح للأجانب يتملكوا في 9 مناطق freehold.',
  },
  
  kuwait: {
    name: 'الكويت',
    nameEn: 'Kuwait',
    currency: 'KWD',
    currencySymbol: 'د.ك',
    locale: 'ar-KW',
    mortgageRate: 6,
    islamicProfitRate: 6.5,
    downPaymentMin: 30,         // % for expats higher
    loanTenureMax: 20,
    avgRentalYield: 5,
    propertyAppreciation: 3,
    inflationRate: 3,
    registrationFeePercent: 0.5,
    avgServiceFees: 600,        // KWD/year
    taxThreshold: 999999999,
    taxRate: 0,
    popularAreas: ['السالمية', 'حولي', 'الجابرية', 'الشعب', 'بيان', 'صباح السالم'],
    notes: 'الأجانب لا يستطيعون تملك عقارات (إلا بقرار خاص). السوق صغير ومستقر.',
  },
  
  bahrain: {
    name: 'البحرين',
    nameEn: 'Bahrain',
    currency: 'BHD',
    currencySymbol: 'د.ب',
    locale: 'ar-BH',
    mortgageRate: 5.5,
    islamicProfitRate: 6,
    downPaymentMin: 20,
    loanTenureMax: 25,
    avgRentalYield: 7,
    propertyAppreciation: 3,
    inflationRate: 2,
    registrationFeePercent: 2,
    avgServiceFees: 800,        // BHD/year
    taxThreshold: 999999999,
    taxRate: 0,
    popularAreas: ['السيف', 'الجفير', 'العدلية', 'الرفاع', 'أمواج'],
    notes: 'الأجانب يقدروا يتملكوا في freehold areas. السوق صغير لكن العائد عالي نسبياً.',
  },
  
  oman: {
    name: 'عمان',
    nameEn: 'Oman',
    currency: 'OMR',
    currencySymbol: 'ر.ع',
    locale: 'ar-OM',
    mortgageRate: 5,
    islamicProfitRate: 5.5,
    downPaymentMin: 20,
    loanTenureMax: 25,
    avgRentalYield: 6,
    propertyAppreciation: 3,
    inflationRate: 2,
    registrationFeePercent: 3,
    avgServiceFees: 500,        // OMR/year
    taxThreshold: 999999999,
    taxRate: 0,
    popularAreas: ['مسقط - الموج', 'القرم', 'الخوض', 'السيب', 'مطرح'],
    notes: 'الأجانب يقدروا يتملكوا في ITCs (Integrated Tourism Complexes). السوق هادي.',
  },
};
```

---

## Yield Benchmarks by Property Type & Area

### مصر — Egypt:
| المنطقة | Apartment Yield | Villa Yield | Notes |
|---------|----------------|-------------|-------|
| القاهرة الجديدة (compounds) | 6-8% | 4-6% | الأكثر استقراراً |
| الشيخ زايد / 6 أكتوبر | 6-8% | 5-7% | demand عالي |
| الساحل الشمالي | 4-7% (موسمي) | 5-9% (موسمي) | يعتمد على summer rental |
| العاصمة الإدارية | 5-7% | 4-6% | جديد، potential عالي |
| المعادي / الزمالك | 5-7% | 4-6% | premium areas |

### السعودية — Saudi Arabia:
| المنطقة | Yield | Notes |
|---------|-------|-------|
| الرياض (أحياء جديدة) | 6-8% | الـ Vision 2030 بتدفع الأسعار |
| جدة (أبحر) | 5-7% | premium area |
| الخبر / الدمام | 6-8% | بترول cities, demand مستقر |

### الإمارات — UAE:
| المنطقة | Yield | Notes |
|---------|-------|-------|
| دبي مارينا | 6-7% | tourist demand |
| داون تاون دبي | 5-6% | luxury, lower yields |
| JVC / Damac Hills | 7-9% | الأعلى yield |
| أبو ظبي - الريم | 6-7% | family-friendly |

---

## Mortgage Tenure Limits

| الدولة | Max Age at Loan End | Max Tenure | Special Schemes |
|--------|--------------------:|-----------:|-----------------|
| مصر | 65 سنة | 20-30 سنة | برنامج البنك المركزي للسكن الاجتماعي |
| السعودية | 70 سنة | 30 سنة | REDF/Sakani للمواطنين |
| الإمارات | 65 (expats) / 70 (citizens) | 25 سنة | — |
| قطر | 65 | 25 سنة | — |
| الكويت | 65 | 20 سنة | بنك الإسكان للمواطنين |

---

## Default Slider Ranges (للـ Dashboard)

```javascript
const SLIDER_RANGES = {
  downPaymentPercent: { min: 10, max: 60, default: 30, step: 5 },
  mortgageRate: { min: 3, max: 30, default: null, step: 0.25 },  // use regional default
  loanYears: { min: 5, max: 30, default: 20, step: 1 },
  occupancyRate: { min: 50, max: 100, default: 90, step: 5 },
  maintenancePercent: { min: 0.5, max: 3, default: 1, step: 0.1 },
  managementPercent: { min: 0, max: 15, default: 8, step: 1 },
  appreciationRate: { min: 0, max: 25, default: null, step: 0.5 },  // use regional
  holdingYears: { min: 1, max: 30, default: 10, step: 1 },
};
```

---

## Off-plan Risk Factors

العقارات تحت الإنشاء (off-plan) شائعة جداً، خصوصاً في:
- مصر (العاصمة الإدارية، صبور، إعمار، طلعت مصطفى)
- الإمارات (Damac، Emaar، Sobha)
- السعودية (NEOM، ROSHN)

### Risks لإضافتها في Tab 3 (Comparison):

| Risk Type | Weight | شرح |
|-----------|--------|-----|
| Delivery delay | High | متوسط التأخير في مصر 1-3 سنين |
| Developer reputation | Critical | تحقق من سجل المطور |
| Quality at handover | Medium | الـ specs على الورق قد تختلف |
| Payment plan vs cash discount | Medium | بعض المطورين بيدوا خصم 10-15% للكاش |
| Currency risk (Egypt esp.) | High | لو القسط بالجنيه والمشروع متأثر بالدولار |

في الـ Dashboard:
```javascript
if (property.status === 'off-plan') {
  // add risk discount to the property's score
  // typically reduce score by 10-15 points
  // show explicit warning in the card
}
```

---

## Currency Conversion (للـ Dashboard لو فيه multi-currency)

استخدم تقريبية مرجعية (قابلة للتعديل):

```javascript
const APPROX_RATES_TO_USD = {
  EGP: 50,    // 1 USD ≈ 50 EGP (تقريبي 2025-2026)
  SAR: 3.75,  // pegged
  AED: 3.67,  // pegged
  QAR: 3.64,  // pegged
  KWD: 0.31,  // 
  BHD: 0.376, // pegged
  OMR: 0.385, // pegged
};
```

> **مهم**: لمصر تحديداً، السعر متقلب. لو المستخدم قال أرقام في الـ chat، اتاكد من الـ exchange rate الحالي قبل أي مقارنة عالمية.

---

## Quick Sanity Checks للأرقام

عند الـ output في الـ Dashboard، تأكد من:

1. **Yield معقول**: لو الـ yield أعلى من 15% → غالباً غلط في الـ inputs
2. **Mortgage payment معقول**: لو القسط أكتر من 60% من الدخل → red flag
3. **Down payment ratio**: لو أقل من 10% → في معظم الدول مستحيل، اعرض warning
4. **Holding period**: لو حد بيشتري ليبيع في أقل من 3 سنين → عادة خسارة بسبب الـ transaction costs

---

## مراجع مفيدة (للمستخدم لو طلب يعرف أكتر)

- **مصر**: عقارماب (Aqarmap)، Property Finder، بايلون، نواعم — للأسعار
- **السعودية**: عقاري (Akari)، Bayut KSA، عقار بلس — للأسعار
- **الإمارات**: Bayut، Property Finder، Dubizzle — للأسعار + market reports
- **التمويل**: مقارنة قروض على [بنوك مصر / SAMA / UAE Central Bank]

في الـ Dashboard Tab 6، اعرض links مرجعية حسب الدولة.
