# Exa MCP Research Reference — استخدام البحث المتعمق للعقارات

دليل مرجعي تفصيلي لاستخدام Exa MCP لتعزيز جودة البيانات في الـ Real Estate Dashboard. اقرأ Phase 0.5 من الـ SKILL.md أولاً للـ workflow، وارجع لهنا للتفاصيل والـ query patterns.

---

## أدوات Exa المتاحة

Exa MCP يوفّر **أداتين فقط** — لا تخترع أسماء أخرى:

| الأداة | الاستخدام |
|--------|-----------|
| `Exa:web_search_exa` | بحث neural/semantic عبر الويب — يرجّع قائمة URLs مع snippets |
| `Exa:web_fetch_exa` | قراءة محتوى URL كامل — للتفاصيل بعد البحث |

> ⚠️ لو شفت أدوات بأسماء `deep_researcher_*`، `company_research_*`، `crawling_*`، أو `linkedin_*` تحت namespace Exa، **شك في المصدر**. الأسماء دي مش جزء من Exa MCP الأساسي.

---

## Pattern موصى به: Search ثم Fetch

```javascript
// Step 1: Neural search لتحديد أفضل URLs
const searchResults = await web_search_exa({
  query: "current apartment prices Hadayek October Cairo 2026",
  numResults: 8
});

// Step 2: اختار 2-3 URLs الأنسب وقراءتها بالتفصيل
const topUrls = searchResults
  .filter(r => r.url.match(/aqarmap|propertyfinder|bayut/))
  .slice(0, 3)
  .map(r => r.url);

const fullContent = await web_fetch_exa({
  urls: topUrls,
  maxCharacters: 5000  // لكل URL
});
```

---

## Query Templates حسب نوع السؤال

### 1. أسعار السوق الحالية

✅ كويسة:
```
"current apartment prices [area] [city] [year] per square meter"
"villa prices compound [area] [city] [year] EGP/SAR/AED"
"studio apartment cheapest [area] [year]"
```

❌ سيئة:
- "real estate prices" (عام جداً)
- "price" (مش محدد)

### 2. معدلات الإيجار

```
"monthly rent [area] [property type] [year]"
"rental price 1 bedroom apartment [area] furnished"
"compound rent vs standalone building [area]"
```

### 3. نسب الفائدة البنكية

```
"mortgage interest rate [country] commercial banks [year]"
"Islamic home financing rate [country] banks [year]"
"home loan tenure maximum [country] [year]"
```

### 4. مطوّرين ومشاريع (Off-plan)

```
"[Developer name] [Project name] payment plan reviews [year]"
"[Developer name] delivery delays history [year]"
"new launches [city] [year] off-plan compound"
```

أمثلة من السوق:
- مصر: Talaat Moustafa, Emaar Misr, SODIC, Hassan Allam, Mountain View
- السعودية: ROSHN, NEOM, Saudi Real Estate, Dar Al Arkan
- الإمارات: Emaar, Damac, Sobha, Aldar, Dubai Properties

### 5. yields ومقارنات الاستثمار

```
"rental yield comparison [area1] vs [area2] [year]"
"highest rental yield areas [city] [year] investor"
"property appreciation rate [city] last 5 years"
```

### 6. تقارير السوق

```
"[city] real estate market report Q[1-4] [year]"
"property price index [country] [year]"
"housing affordability index [country] [year]"
```

---

## Domain Filters المفيدة

### مصر:
- aqarmap.com.eg (الأشمل)
- propertyfinder.eg
- nawy.com

### السعودية:
- aqar.fm
- bayut.sa
- propertyfinder.sa

### الإمارات:
- bayut.com
- propertyfinder.ae
- dubizzle.com

### قطر/البحرين/الكويت:
- propertyfinder.qa
- propertyfinder.bh
- bayut.com.kw

### مصادر اقتصادية (للـ context):
- enterprise.press (مصر)
- argaam.com (السعودية)
- zawya.com (الإقليمي)

---

## Source Attribution في الـ Dashboard

لما تستخدم بيانات حية من Exa، اعرض المصدر في الـ Dashboard بشكل واضح:

```html
<div style="margin-top:12px; padding:8px 12px; background:var(--color-background-secondary); border-radius:8px; font-size:11px;">
  <i class="ti ti-database" style="font-size:12px" aria-hidden="true"></i>
  بيانات السوق من:
  <a href="https://aqarmap.com.eg/...">Aqarmap</a>
  • <a href="https://propertyfinder.eg/...">Property Finder</a>
  <br>
  محدّث: 20 مايو 2026 • عبر Exa MCP
</div>
```

**ليه ده مهم:**
1. الشفافية — المستخدم يفهم الرقم جه منين
2. التحقق — يقدر يفتح الرابط ويراجع بنفسه
3. التاريخ — الأسعار بتتغير، يعرف لو الرقم قديم

---

## Caching & Rate Limiting

### قواعد الاستهلاك:

- **حد أقصى 3-5 Exa calls** في الـ workflow الواحد للـ dashboard
- **متعملش retries غبية** — لو query رجع نتائج ضعيفة، غيّر الـ wording مش تكرر نفسه
- **Cache في الـ session**: لو سألت عن أسعار حدائق أكتوبر turn واحد، اللي بعده ما تسألش تاني

### Pattern موصى به للـ Dashboard build:

```
1. Phase 0.5: tool_search → اتأكد إن Exa متاح
2. عمل max 2 search queries مختلفة (سعر + إيجار)
3. لو محتاج تفاصيل عقار محدد: web_fetch_exa على 1-2 URLs
4. اجمع البيانات واستخدمها في الـ Dashboard
5. ما تفضلش تبحث على كل property card — استخدم رنجات
```

---

## أمثلة End-to-End

### مثال 1: "بدور على شقة في حدائق أكتوبر بـ 1.5 مليون"

```
Step 1: tool_search("exa web search") → Exa:web_search_exa موجود

Step 2: web_search_exa({
  query: "Hadayek October apartment 1.5 million EGP studio 1 bedroom 2026",
  numResults: 8
})
نتائج من Aqarmap، Property Finder، عقاركم
استخراج: studios 1.1-1.4M، 1BR 1.6-2M

Step 3: web_fetch_exa({
  urls: ["https://aqarmap.com.eg/...search-results", "https://propertyfinder.eg/..."],
  maxCharacters: 4000
})
تفاصيل listings فعلية، أسعار متر، تشطيب، compounds

Step 4: ادمج في الـ Dashboard:
- Tab 3 (Comparison): 3-4 properties حقيقية من البحث
- Tab 4 (ROI): لو الهدف استثمار، yields من معدلات إيجار السوق
- Source attribution في كل tab
```

### مثال 2: "العقار ده كويس؟ سعره 2.5 مليون في الشيخ زايد، إيجاره 12 ألف شهرياً"

```
Step 1: Exa check

Step 2: web_search_exa({
  query: "Sheikh Zayed apartment rental yield 2.5 million 2026 investor"
})
متوسط السوق: yields 5-7% للشقق في الشيخ زايد

Step 3: المستخدم بيقول 12k/month = 144k/سنة على 2.5M = 5.76% gross
في حدود السوق، مش استثناء

Step 4: في الـ Dashboard Tab 4:
- اعرض yields الحقيقية كـ benchmark
- مقارنة الـ yield الحالي vs متوسط المنطقة
- Tab 6 (Recommendation): "yield قريب من متوسط المنطقة — استثمار عادي مش استثناء"
```

### مثال 3: "Talaat Moustafa Madinaty — العرض الجديد كويس؟"

```
Step 1: Exa check

Step 2: web_search_exa({
  query: "Talaat Moustafa Madinaty new launch payment plan 2026 reviews delivery"
})
معلومات عن:
- الـ payment plan الحالي (مقدم 5-10%، تقسيط 8-10 سنين)
- تاريخ التسليم
- سمعة المطور (delivery track record)

Step 3: web_fetch_exa على 2 URLs أعلى quality للتفاصيل

Step 4: في الـ Dashboard:
- اعرض الـ specs الحقيقية للعرض
- اعرض الـ risks (off-plan delay history لو فيه)
- اعرض cash discount alternative لو فيه
```

---

## Disclaimer Pattern

في الـ Dashboard، أضف Note واضح:

> "البيانات الحية مأخوذة من بحث Exa MCP بتاريخ [date]. الأسعار الفعلية بتتغير يومياً وممكن تكون مختلفة عن العقار الحقيقي. تحقق من المصدر مباشرة قبل أي قرار."

---

## Fallback Behavior لو Exa مش متاح

استخدم `web_search` العادي بنفس الـ queries، لكن:

1. **اعمل أكتر searches** (4-6 بدل 2-3) عشان تغطي زوايا مختلفة
2. **استخدم `site:` operator**: `"apartment Hadayek October site:aqarmap.com.eg"`
3. **توقع نتائج عامة أكتر** — defaults من regional-data.md ممكن تكون أحسن من نتائج ضعيفة

في حالات نادرة، لو محدش متاح (لا Exa لا web_search):
- استخدم defaults بس
- نبّه المستخدم: "ما قدرتش أجيب أرقام حية — الأرقام في الـ Dashboard مرجعية من قاعدة بياناتي"
