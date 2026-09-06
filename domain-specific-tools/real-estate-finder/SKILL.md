---
name: real-estate-finder
description: |
  مهارة إيجاد العقار المناسب وتحليل القدرة الشرائية والاستثمار العقاري — Real Estate Finder & Affordability Analyzer. استخدم هذه المهارة كل مرة يذكر فيها المستخدم: شراء شقة، استئجار شقة، البحث عن عقار، بدور على بيت، عاوز أشتري شقة، استثمار عقاري، شقق للبيع/للإيجار، فيلا، دوبلكس، استوديو، rental yield، ROI عقاري، rent vs buy، أأجر ولا أشتري، حساب القدرة الشرائية، affordability، رهن عقاري، تمويل عقاري، mortgage، تمويل إسلامي، مقارنة عقارات، أو أي قرار شراء/إيجار/استثمار عقاري في مصر أو الخليج (السعودية، الإمارات، قطر، الكويت، البحرين، عمان). استخدمها أيضاً عند: "هل أشتري ولا أأجر؟"، "إيه أفضل منطقة أستثمر فيها؟"، "ميزانيتي X هل تكفي لشقة في Y؟"، "كم لازم أوفر علشان أشتري؟"، مقارنة بين عقارين أو أكثر، أو تقييم عقار من ناحية الـ ROI. حتى لو المستخدم ما طلبش dashboard صراحة، استخدم هذه المهارة لأن الناتج الأساسي هو dashboard تفاعلي مدعوم ببيانات سوق حية (عبر Exa MCP لو متاح، أو web_search كـ fallback) مش رد نصي.
---

# Real Estate Finder — مستشار العقارات والقدرة الشرائية

## فلسفة الـ Skill

> **العقار قرار كبير — مش لازم يكون قرار صعب.**
> هدفنا نخلي المستخدم يدخل قرار العقار وعنده الـ data والـ analysis اللي يخليه يقرر بثقة، مش بناءً على إحساس أو ضغط من سمسار.

اللي بنعمله في 3 خطوات:
1. **نجمع/نستنتج التفضيلات** (وين، ليه، إيه نوع العقار)
2. **نجمع البيانات المالية** — أو نتيح للمستخدم يجربها بنفسه بدون ما يكتبها لو مش مرتاح
3. **نطلع Interactive Dashboard** بكل التحليلات والتوصيات

> ⚠️ **الـ deliverable الأساسي للـ skill هو الـ Dashboard الـ artifact — مش رد نصي طويل في الـ chat.** خلي ردك في الـ chat قصير ومركز، والـ dashboard هو اللي بياخد كل التفاصيل.

---

## ⚠️ مبدأ الخصوصية الأساسي

البيانات المالية حساسة جداً. قاعدة ذهبية:

| الموقف | الإجراء |
|--------|---------|
| المستخدم شارك أرقامه طوعاً | استخدمها كـ baseline قابل للتعديل في الـ dashboard |
| المستخدم رفض / متحفظ | **متضغطش عليه**. اعمل الـ dashboard بـ default values معقولة و sliders يجربها بنفسه |
| المستخدم قال "مش متأكد" | استخدم defaults إقليمية + اشرحه ليه واخليه يعدل |

> الأرقام الحساسة (الدخل، الأقساط، الديون) **ما تبقاش مذكورة في رد الـ chat** — تبقى بس في الـ dashboard اللي بيتحكم فيه المستخدم.

---

## Phase 0: Smart Context Gathering — قبل ما تسأل أي حاجة

قبل أي سؤال، استفيد من اللي عندك:

1. **Memory check** — لو فيه `mem` connector، شوف لو فيه ذكر سابق لخطط عقارية أو ميزانية أو دولة
2. **Chat history** — اقرا السياق كويس، يمكن المستخدم ذكر:
   - مدينة/دولة (e.g., "أنا في الرياض")
   - رقم تقريبي ("عندي 2 مليون")
   - الهدف ("للسكن" / "استثمار" / "مصيف")
   - الحالة العائلية أو عدد الأفراد
3. **Location signal** — لو موقع المستخدم متاح في الـ system context، ابدأ منه

### قاعدة ذهبية:
> **استنتج أكتر ما تسأل.** بس لو استنتجت غلط، اذكر الافتراض صراحة: "افترضت إنك في القاهرة بناءً على المحادثة — صح؟"

---

## Phase 0.5: Live Market Research — هل بياناتك حية؟ (مهم)

> الـ defaults في `references/regional-data.md` تقريبية ومرجعية. السوق العقاري — خاصة المصري — متقلب جداً، وأرقام من 6 شهور = ممكن تكون قديمة. لازم تحاول تجيب بيانات حية للحالات الجدية.

### Step 1: افحص هل Exa MCP متاح في الـ session

في أول turn فيها سؤال عقاري جدي، شغّل:

```
tool_search(query="exa web search")
```

**Exa فيه tool اتنين بس** — اعتمد عليهم:
- `Exa:web_search_exa` — neural/semantic search (أحسن من Google للأسئلة الطبيعية)
- `Exa:web_fetch_exa` — قراءة URLs كاملة (للتفاصيل بعد البحث)

> ⚠️ **لا تخترع أسماء tools.** Exa مفيهوش `deep_researcher` ولا `company_research`. لو شفت أسماء غير الاتنين دول، شك في المصدر.

**تحليل النتيجة:**

| النتيجة | يعني | الإجراء |
|---------|------|---------|
| ظهرت `Exa:web_search_exa` و `Exa:web_fetch_exa` | Exa متاح ✅ | استخدمه أداة البحث الأساسية |
| ظهرت Apify (`rag-web-browser`) بس | Exa مش مفعّل | استخدم `web_search` العادي |
| مفيش أي أداة بحث | session بسيط | استخدم `web_search` العادي لو متاح، أو defaults فقط |

### Step 2: متى تستخدم Exa؟ (لازم تكون انتقائي)

البحث بياخد وقت وtokens. استخدم Exa **بس** في الحالات دي:

1. **المستخدم بيقيّم عقار محدد** — "الكومباوند ده، السعر ده، رأيك إيه؟"
2. **مقارنة مناطق محددة** — "القاهرة الجديدة vs الشيخ زايد"
3. **سؤال عن مطور/مشروع بالاسم** — طلعت مصطفى، إعمار، صبور، روشن
4. **المستخدم شكّك في الأرقام** — "الـ yields دي مش حاسس إنها صح"
5. **العقار في منطقة جديدة/متغيرة** — العاصمة الإدارية، نيوم، dubai south

**ما تستخدمش Exa لو:**
- السؤال نظري/استكشافي ("لو دخلي X هقدر أشتري إيه؟") — defaults كافية
- المستخدم في عجلة وعاوز dashboard فوراً
- مفيش منطقة محددة لسه

### Step 3: Queries فعّالة لـ Exa

Exa neural search — اكتب اللي تدور عليه بطريقة طبيعية، مش keywords:

**أمثلة شغّالة:**
```
web_search_exa({ 
  query: "current apartment prices Hadayek October Cairo 2026 per square meter",
  numResults: 8 
})

web_search_exa({ 
  query: "Talaat Moustafa Madinaty 1 bedroom payment plan reviews 2026" 
})

web_search_exa({ 
  query: "Egypt mortgage interest rates commercial banks home loans 2026" 
})

web_search_exa({ 
  query: "Dubai Marina vs JVC rental yield comparison 2026 investor" 
})
```

ثم `web_fetch_exa` على أفضل 2-3 URLs للقراءة بالتفصيل:
```
web_fetch_exa({ 
  urls: ["https://aqarmap.com/...", "https://propertyfinder.eg/..."],
  maxCharacters: 5000 
})
```

### Step 4: ادمج النتائج في الـ Dashboard

- **Property cards** (Tab المقارنة): استبدل الـ sample properties بـ listings حقيقية من Exa
- **Regional defaults** (interest rate, yields): لو لقيت أرقام محدّثة، عدّل الـ defaults
- **قسم "المصادر"**: أضف قسم صغير في آخر الـ Dashboard فيه links للـ URLs اللي رجعت — شفافية للمستخدم
- **اذكر التاريخ**: لو Exa رجّعت أسعار من Q3 2025، قول للمستخدم كده

### Step 5: Fallback Chain لو Exa مش متاح

```
priority 1: Exa:web_search_exa + Exa:web_fetch_exa  ← الأفضل
priority 2: web_search (built-in)                    ← مقبول
priority 3: defaults من regional-data.md             ← آخر ملاذ
```

**رسالة للمستخدم لو Exa مش متاح:**
> "ملاحظة: Exa MCP بيدي نتائج أدق للعقارات. لو متاح في الـ connectors بتاعتك، فعّله للحصول على بيانات سوق حية. هكمّل دلوقتي بـ web search عادي/defaults."

---

## Phase 1: Preferences Collection — جمع التفضيلات

اجمع المعلومات بالحوار الطبيعي (مش form). دمج 2-3 أسئلة في رسالة واحدة بدل ما تسأل واحد واحد.

### المعلومات الأساسية (لازم):
1. **الدولة والمدينة/المنطقة** — مثلاً: القاهرة الجديدة، الساحل الشمالي، الرياض الشمالية، دبي مارينا، الخبر
2. **الهدف الأساسي**:
   - 🏠 **سكن شخصي** — أنا/أسرتي هنسكن فيه
   - 💰 **استثمار للإيجار** — هأجره وأكسب دخل شهري
   - 📈 **استثمار للبيع** — capital appreciation (هحتفظ سنين وأبيع)
   - 🏖️ **مصيف/بيت تاني** — للاستخدام الموسمي
3. **شراء أم إيجار** — أو "مش عارف، عاوز أقارن"

### المعلومات الثانوية (اسأل لو محتاج بس):
4. **نوع العقار** — شقة / فيلا / دوبلكس / استوديو / تجاري
5. **المساحة وعدد الغرف** — تقريباً
6. **الميزانية التقريبية** — range أوكي (من-إلى)
7. **الجدول الزمني** — دلوقتي / 6 شهور / سنة
8. **متطلبات خاصة** — قريب من شغل/مدارس، compound، إطلالة، تشطيب، إلخ

### Output of Phase 1: Profile Card (في الـ chat، مختصر)

```
═══════════════════════════════════════
   🏘️  Real Estate Profile
═══════════════════════════════════════
🌍 الدولة/المدينة:  [...]
🎯 الهدف:           [سكن / استثمار-إيجار / استثمار-بيع / مصيف]
🔑 القرار:          [شراء / إيجار / مقارنة]
🏠 النوع:           [...]
📐 المساحة:         [...] م²
🛏️  الغرف:          [...]
💰 الميزانية:       [range]
📅 التوقيت:         [...]
═══════════════════════════════════════
```

---

## Phase 2: Financial Profile — البيانات المالية

⚠️ **قبل أي سؤال مالي، قل للمستخدم بوضوح:**

> "علشان أحسبلك القدرة الشرائية بدقة، محتاج كام رقم. لو مش مرتاح تشاركهم هنا، **مفيش مشكلة خالص** — هعملك Dashboard تفاعلي تحط فيه الأرقام بنفسك وتجرب سيناريوهات مختلفة بدون ما تكتبها في الشات."

### المعلومات المثالية (لو وافق):
1. **الدخل الشهري الصافي** — بعد الضرائب
2. **السيولة المتاحة (الكاش)** — للـ down payment
3. **المصاريف الشهرية** — تقريباً (أكل، مواصلات، فواتير، إلخ)
4. **الالتزامات الشهرية** — أقساط قروض، بطاقات ائتمان، إلخ
5. **دخل إضافي؟** — شغل تاني، إيجار، إلخ
6. **هل عنده تمويل بنكي متاح؟** — أو cash فقط؟ تمويل إسلامي؟

### Decision Tree للتعامل مع المعلومات:

| الموقف | الإجراء |
|--------|---------|
| شارك كل البيانات | استخدمها كـ baseline في الـ dashboard مع إمكانية التعديل |
| شارك جزء بس | استخدم اللي شارك + الباقي defaults إقليمية |
| رفض المشاركة | كل الـ dashboard بـ defaults + sliders — **متذكرش أي رقم شخصي في الـ chat** |
| قال "مش عارف" | اعرض defaults معقولة للدولة وخليه يعدل |

---

## Phase 3: The Interactive Dashboard — الـ Artifact الأساسي

### ⚠️ ده الـ deliverable الأساسي. ركز عليه.

اعمل **HTML/React artifact واحد single-file** بالمواصفات دي:

#### Tech Stack
- React (functional components + hooks)
- Tailwind CSS (utility classes فقط)
- `recharts` للـ charts
- `lucide-react` للـ icons
- لا تستخدم localStorage/sessionStorage (مش مدعوم في الـ artifacts)
- كل الحالة في React state

#### المواصفات الإجبارية:
1. **RTL support** — يدعم العربي والإنجليزي مع toggle button في الـ header
2. **Mobile-first responsive** — يشتغل ممتاز على الموبايل
3. **Real-time calculations** — أي تغيير في input يحدث كل الـ outputs فوراً
4. **Color-coded health indicators**:
   - 🟢 أخضر = ممتاز (e.g., housing < 25% of income)
   - 🟡 أصفر = مقبول (25-33%)
   - 🔴 أحمر = خطر (>33%)
5. **Currency formatting** حسب الدولة (EGP, SAR, AED, إلخ)
6. **Tooltips** على كل مصطلح مالي (cap rate، yield، إلخ)
7. **State persistence** عبر الـ tabs (React state، مش localStorage)

#### هيكل الـ 6 Tabs:

##### Tab 1: 📋 Profile & Preferences
- يعرض الـ Profile Card قابل للتعديل
- التغييرات تأثر على باقي الـ tabs

##### Tab 2: 💰 Affordability Calculator
**Inputs (sliders + number fields):**
- الدخل الشهري الصافي
- المصاريف الشهرية الحالية
- الالتزامات الشهرية (أقساط قائمة)
- السيولة المتاحة للـ down payment
- نسبة الفائدة المتوقعة (default حسب الدولة من `references/regional-data.md`)
- مدة القرض بالسنوات
- نسبة الـ Down Payment (slider)

**Outputs المحسوبة:**
- أقصى قسط شهري آمن (28/36 rule)
- أقصى قرض ممكن (reverse mortgage formula)
- **أقصى سعر عقار يقدر يشتريه** ← الـ output الأهم
- الـ Down Payment المطلوب بالأرقام
- Total monthly housing cost (قسط + صيانة + رسوم متوقعة)
- Health bar: نسبة الـ housing-to-income

**المعادلات**: `references/financial-frameworks.md`

##### Tab 3: 🆚 Property Comparison
- بطاقات لـ 2-4 عقارات (المستخدم يضيف/يحذف بـ "+ Add Property" button)
- لكل عقار: اسم، موقع، سعر، مساحة، غرف، سنة، حالة (جاهز/تحت إنشاء)، رسوم شهرية متوقعة
- **جدول مقارنة side-by-side** (مع scroll أفقي على الموبايل)
- **Scoring system** — كل عقار يتقيم على:
  - السعر / المتر مقارنة بمتوسط المنطقة
  - الـ Affordability fit (هل يقدر يدفعه؟)
  - الـ ROI لو استثمار
  - تقييم المنطقة (input من المستخدم 1-10)
- **Winner badge** على العقار الأنسب

##### Tab 4: 📈 Investment Analysis (ROI)
**يظهر فقط لو الهدف = استثمار**

**Inputs:**
- سعر العقار
- الإيجار الشهري المتوقع
- معدل الإشغال السنوي (default 90% سكني، 80% مصيفي)
- مصاريف صيانة سنوية (% من القيمة)
- مصاريف إدارة (لو شركة management)
- ضرائب/رسوم سنوية
- معدل التضخم العقاري المتوقع (% سنوياً، default من `references/regional-data.md`)
- Down Payment %
- مدة الاحتفاظ (5/10/15 سنة)

**Outputs:**
- **Gross Rental Yield** = (الإيجار السنوي / السعر) × 100
- **Net Rental Yield** = ((الإيجار السنوي - المصاريف) / السعر) × 100
- **Cash-on-Cash Return**
- **Cap Rate**
- **Break-even point** بالشهور
- **Projection chart**: إجمالي العائد (إيجار + تقدير قيمة) على 5/10/15 سنة (recharts LineChart)
- مقارنة مع الـ regional benchmark (مثلاً: "yields في القاهرة الجديدة عادة 6-8%")

##### Tab 5: 🏠 Rent vs Buy Calculator
**يظهر لو المستخدم متحير أو طلبه صراحة**

Side-by-side:
- **سيناريو الإيجار**: إيجار شهري + ادخار الـ down payment + الفرق الشهري في استثمار بفائدة سنوية معقولة
- **سيناريو الشراء**: قسط + صيانة + رسوم + ضريبة

**Outputs:**
- Total wealth chart على 5/10/15/20 سنة
- **Break-even point** — متى الشراء يبقى أوفر من الإيجار؟
- توصية واضحة بناءً على الـ horizon المخطط

##### Tab 6: 🎯 Smart Recommendation
**ملخص ذكي ومخصص — أهم tab:**
- توصية واضحة بلغة بسيطة: "اشتري"، "أجّر"، "استنى وادخر شهر/سنة"، "حدّد ميزانية أقل بكذا"
- 3-5 أسباب رئيسية
- **Risk factors** للمنطقة/الدولة (تقلب عملة، off-plan risk، إلخ)
- **Next steps**: 3-5 خطوات عملية محددة

---

## Phase 4: Building the Dashboard — التنفيذ

### Step 0: ادمج بيانات Exa لو متاحة (من Phase 0.5)
- لو عملت `web_search_exa` ولقيت أرقام محدّثة لـ interest rates / yields / appreciation → استخدمها بدل defaults من `regional-data.md`
- لو لقيت **listings فعلية** للمنطقة → استبدل الـ sample properties في Tab المقارنة بـ 3-4 منها (مع رابط المصدر)
- لو الـ Exa data تختلف بشكل كبير عن defaults → اعرض الاتنين للمستخدم باختصار: "حسب defaults: X. حسب آخر بيانات السوق: Y"
- في آخر الـ Dashboard، أضف قسم "**المصادر**" صغير فيه links للـ URLs اللي اعتمدت عليها

### Step 1: راجع الـ references قبل ما تكتب الكود
- `references/financial-frameworks.md` — كل المعادلات (mortgage, ROI, affordability)
- `references/regional-data.md` — الـ default values لكل دولة (فايدة، down payment، yields، إلخ)

### Step 2: Frontend Design
راجع `/mnt/skills/public/frontend-design/SKILL.md` قبل ما تبدأ — مهم لأي UI/component.

### Step 3: اكتب الـ artifact
- Single HTML file artifact
- ابدأ بـ tabs structure، بعدين املأ كل tab
- اختبر إن الحسابات صحيحة بـ console.log قبل الـ render

### Critical Patterns:

**State management**:
```javascript
const [userProfile, setUserProfile] = useState({
  country: 'egypt',
  city: '',
  goal: 'living', // living | rental | flip | vacation
  decision: 'buy', // buy | rent | compare
  // ...
});

const [financials, setFinancials] = useState({
  monthlyIncome: 0,
  monthlyExpenses: 0,
  liabilities: 0,
  savings: 0,
  // ...
});
```

**Currency formatting**:
```javascript
const formatCurrency = (amount, country) => {
  const config = REGIONAL_DATA[country];
  return new Intl.NumberFormat(config.locale, {
    style: 'currency',
    currency: config.currency,
    maximumFractionDigits: 0,
  }).format(amount);
};
```

**Mortgage payment** (use everywhere):
```javascript
const monthlyPayment = (principal, annualRate, years) => {
  if (principal <= 0 || years <= 0) return 0;
  const r = annualRate / 12 / 100;
  const n = years * 12;
  if (r === 0) return principal / n;
  return principal * (r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
};
```

**RTL toggle**:
```javascript
const [lang, setLang] = useState('ar');
const isRTL = lang === 'ar';
<div dir={isRTL ? 'rtl' : 'ltr'} className="...">
```

---

## Conversation Flow Triggers

| المستخدم قال | اعمل |
|--------------|------|
| "عاوز أشتري شقة" / "بدور على عقار" | Phase 0 → **Phase 0.5 (check Exa)** → Phase 1 → Phase 2 → Dashboard كامل |
| "بدور على شقة في X بميزانية Y" | Phase 0 → **Phase 0.5 (Exa للأسعار في X)** → Phase 1 (اللي ناقص) → Phase 2 → Dashboard |
| "هل أأجر ولا أشتري؟" | Phase 1 سريع → Phase 2 → Dashboard مع التركيز على Tab 5 (Exa غير ضروري) |
| "عاوز أستثمر في عقار" | Phase 1 (هدف=استثمار) → **Phase 0.5 (Exa للـ yields)** → Phase 2 → Dashboard Tab 4 |
| "العقار ده كويس؟ سعره X" | اطلب التفاصيل → **Phase 0.5 (Exa للتحقق من السعر والـ yields)** → Dashboard |
| "كم لازم أوفر علشان شقة بـ X؟" | Phase 1 مختصر → Phase 2 → Dashboard Tab 2 (Exa غير ضروري) |
| "قارنلي بين عقارين/تلاتة" | Phase 1 → **Phase 0.5 (Exa للتحقق من الأسعار)** → Phase 2 → Dashboard Tab 3 |
| "إيه أحدث أسعار العقارات في X؟" | **Phase 0.5 إجباري** → عرض النتائج → اقترح dashboard |

---

## ⚠️ Important Notes & Disclaimers

### في الـ Dashboard لازم يكون فيه disclaimer واضح:
> "الأرقام دي تقريبية ومرجعية — مش بديل عن استشارة مستشار عقاري أو محامي قبل أي قرار شراء. الفوائد والـ yields والـ benchmarks بتتغير. راجع الأرقام مع البنك/المسوّق العقاري قبل التوقيع."

### اعتبارات خاصة بالمنطقة:
- **مصر**: تقلب عملة كبير — أضف disclaimer واضح في الـ Affordability tab لو القرض بالجنيه والعقار سعره بيتأثر بالدولار
- **الخليج**: التمويل الإسلامي شائع — اعرضه كـ option في الـ Affordability tab بـ toggle (مرابحة vs قرض تقليدي)
- **Off-plan vs Ready**: العقارات تحت الإنشاء (off-plan) شائعة جداً في مصر/الخليج — أضف risk factor في Tab 3 (Comparison) لو العقار off-plan
- **رسوم التسجيل**: مصر ~2.5%، السعودية 5% VAT للعقارات الجديدة، الإمارات 4% DLD — أضفها في الـ total cost
- **خصوصية ثقافية**: في الخليج، الـ compounds والـ family-friendly مهم — Tab 3 يديها وزن

### مبدأ الذكاء:
- متخوضش في كل تفصيلة في الـ chat — الـ dashboard هو المكان الصح
- لو المستخدم سأل سؤال محدد عن رقم في الـ dashboard، رد سريع وارجع للـ dashboard
- لو المستخدم محتاج يعدل الـ dashboard، عدل الـ artifact، متعملش رد نصي جديد طويل

---

## Reference Files

- `references/financial-frameworks.md` — المعادلات الكاملة (Mortgage, ROI, Affordability rules, Rent-vs-Buy formula)
- `references/regional-data.md` — أرقام مرجعية لكل دولة (mortgage rates, down payments, yields, appreciation, fees)
- `references/exa-research.md` — استخدام Exa MCP للبحث المتعمق (query templates، source attribution، fallback strategy، end-to-end examples)
- `references/exa-research.md` — Library of tested Exa queries لكل use case (أسعار، إيجارات، مطورين، فوائد بنكية)
