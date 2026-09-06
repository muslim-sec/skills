# Era Context Toolkit — دليل أدوات Era الكامل لـ Goal Architect

> هذا الـ reference يفصّل كل tool من tools Era Context اللي بنستخدمها في الـ Skill، متى نستدعيه، إيه parameters المهمة، وإيه نمط الاستخدام الأمثل.

---

## مبدأ عام: قلل الـ Round Trips

كل استدعاء tool = round trip. اجمع البيانات بأقل عدد ممكن من الاستدعاءات.

**Anti-pattern (لا تفعل):**
```
1. list_financial_accounts (لكل حساب)
2. check_account_balance (لكل حساب)  
3. list_transactions (آخر شهر)
4. analyze_spending (شهر بشهر، شهر شهر)
5. ...
```

**Pattern صحيح:**
```
1. knowledge__get_financial_context_and_overview  ← يعطي 80% مما تحتاج
2. (لو محتاج تفاصيل) → استدعِ tool واحد محدد
```

---

## 🌟 Tier 1: لازم تستدعيهم في كل session

### `knowledge__get_financial_context_and_overview`

**متى:** أول tool تستدعيه في كل session. **دايماً.**

**يرجع:**
- الـ user profile
- كل الحسابات وأرصدتها
- الـ net worth
- ملخص الـ cash flow
- معلومات الـ subscriptions/recurring (لو متاحة)

**كيف تستخدم الناتج:**
- لو الـ overview كافي → اكمل لـ Phase 3 (Elicit)
- لو فيه فجوات (مثلاً: profile incomplete) → استدعِ `get_pending_questions`
- لو محتاج تفاصيل أعمق → استدعِ الـ tier 2 tools

---

## 🥈 Tier 2: حسب الحاجة

### `insights__get_cash_flow`

**متى:** لما الـ overview ما رجّعش cash flow كافٍ، أو لما تحتاج رؤية شهر-بشهر.

**Parameters مهمة:**
- `period`: عادة `last_6_months` كافي لـ baseline
- لو الـ income متغير، خد `last_12_months`

**استخراج:**
- متوسط الدخل الشهري
- متوسط المصاريف الشهري
- الـ surplus/deficit pattern

---

### `insights__analyze_spending`

**متى:** قبل Phase 5 (Optimization). لازم تشوف المصاريف بالـ category.

**Parameters:**
- `group_by`: `category` (الأهم) — ممكن كمان `merchant` أو `account`
- `period`: `last_3_months` (يوازن بين الدقة والـ relevance)

**استخراج:**
- top 6 categories (للـ pie chart في Tab 2)
- top merchants (لو الـ user محتاج يشوف بيصرف فين بالظبط)

> ⚠️ **مهم:** المصاريف على الكهرباء والإيجار categories إجبارية — متقترحش تقليلها (الـ skill بتقترح تحسين الـ discretionary فقط)

---

### `transactions__list_recurring_charges`

**متى:** قبل Phase 5، خصوصاً المستوى "محافظ". الاشتراكات المتكررة هي الـ low-hanging fruit.

**يرجع:**
- list of subscriptions/recurring payments
- frequency (monthly/yearly)
- last charge date
- merchant name

**استخدام:**
- ابحث عن duplicates (Netflix + Shahid + Disney+؟)
- ابحث عن خدمات مش مستخدمة (آخر استخدام لها متى؟)
- اعمل قائمة "Quick wins" في Tab 4

> **مثال على الإخراج المتوقع:**
> ```
> - Netflix Premium: 200 EGP/شهر (آخر شحن: 3 أيام)
> - Shahid VIP: 150 EGP/شهر
> - OSN+: 250 EGP/شهر
> ⚠️ duplicate detected: عندك 3 streaming خدمات. ينفع تخلي 1-2 بدل 3.
> ```

---

### `insights__compare_spending_periods`

**متى:** Phase 8 (Follow-up). أو لما المستخدم يقول "كنت بصرف أكتر السنة اللي فاتت، صح؟"

**Parameters:**
- `period_a`: قبل بدء الهدف
- `period_b`: بعد بدء الهدف

**استخراج:**
- هل المستخدم فعلاً قلل من المصاريف اللي اتفقنا عليها؟
- في categories تانية زادت بشكل غير متوقع؟ (compensatory spending)

---

## 🥉 Tier 3: استخدام خاص

### `accounts__list_financial_accounts`

**متى:** لو الـ overview ما رجّعش الحسابات بالتفصيل، أو لو محتاج معرفة hidden balances.

**استخراج:**
- لكل حساب: النوع (checking/savings/credit/investment)
- الرصيد الحالي
- العملة

> **مهم:** لو فيه حساب توفير منفصل، اعرضه كـ "starting point" للهدف في Tab 1.

---

### `accounts__check_account_balance`

**متى:** نادر. بس لو محتاج رصيد real-time لحساب معين (مثلاً قبل Phase 6 لتأكيد الـ savings الحالية).

**Anti-pattern:** ما تستدعيش لكل حساب — استخدم `list_financial_accounts` بدلاً منها.

---

### `insights__forecast_spending`

**متى:** Phase 3-4، لو المستخدم سأل "هل دخلي هيكفي للشهر الجاي؟" أو لو محتاج توقع للـ feasibility.

**استخراج:**
- المصاريف المتوقعة للـ end of period
- مقارنتها بالـ income المتوقع

---

### `transactions__search_transactions` / `list_transactions`

**متى:** لو المستخدم سأل سؤال محدد جداً عن transaction معين، أو عاوز يتحقق من merchant معين.

**Anti-pattern:** ما تستخدمش للـ general analysis — `analyze_spending` أفضل وأخف.

---

## 🧠 Knowledge Tools

### `knowledge__get_pending_questions`

**متى:** بعد `get_financial_context_and_overview` لو فيه فجوات.

**استخراج:**
- الأسئلة اللي Era محتاجة إجابات ليها

**كيف تتعامل:**
- اعرض على المستخدم الأسئلة كـ batch
- استخدم `knowledge__show_question_ui` للأسئلة المعقدة (numeric, date)
- استخدم `knowledge__remember` للأسئلة البسيطة (text, boolean)

---

### `knowledge__remember`

**متى:** Phase 7 (Commit) — لحفظ الهدف.

**كيف تحفظ:**

```
content: "هدف: [اسم الهدف] | المبلغ: [X EGP] | الإطار الزمني: [N شهر] | تاريخ البدء: [YYYY-MM-DD] | تاريخ النهاية المتوقع: [YYYY-MM-DD] | الادخار الشهري المطلوب: [Y EGP] | مستوى التحسين: [محافظ/متوسط/عدواني]"
```

> **مهم:** خلي الـ content structured وواضح علشان يبقى قابل للـ parse لما `recall_history` يستدعيه.

### يمكن كمان حفظ:
- **Preferences:** "المستخدم يفضل التمويل الإسلامي على القرض التقليدي"
- **Constraints:** "المستخدم له ابن في الجامعة، التعليم اساسي في الميزانية"
- **Wins:** "حقق المستخدم 25% من هدف العربية في شهرين"

---

### `knowledge__recall_history`

**متى:** Phase 8 (Follow-up). لما المستخدم يرجع.

**استخدام:**
- ابحث عن "هدف:" في الـ facts
- استخرج الـ structured data من الـ content
- قارن الـ start date بالتاريخ الحالي → اعرف "أين هو الآن مقابل الخطة"

---

## 🚫 Tools نادراً نستخدمها

### `connections__connect_bank_account`
- بس لو المستخدم قال "Era مش بتشوف حسابي الجديد"
- متفترحش بنفسك — استنى من المستخدم

### `transactions__import_csv_transactions`
- بس لو المستخدم بنفسه قال "عندي ملف CSV من البنك"
- ما تطلبش CSV بشكل تلقائي

### `connections__disconnect_institution`
- ما تستخدمها أبداً تلقائياً — destructive action
- لو المستخدم طلبها صراحة، أكد قبل التنفيذ

### `knowledge__forget`
- بس لو المستخدم قال "احذف الهدف ده" أو "متفتكرش الـ X ده"
- destructive — أكد قبل التنفيذ

---

## 📋 Workflow Reference: الـ Tool Calls حسب الـ Phase

| Phase | الأدوات الأساسية | الأدوات الاحتياطية |
|-------|--------------------|----------------------|
| 2 (Diagnose) | `get_financial_context_and_overview` | `get_cash_flow`, `analyze_spending`, `list_recurring_charges` |
| 3 (Elicit) | (محادثة، مش tools) | `get_pending_questions` لو فيه فجوة |
| 4 (Feasibility) | (حساب محلي بالـ JS في الـ artifact) | `forecast_spending` لو معلومات ناقصة |
| 5 (Optimize) | `analyze_spending`, `list_recurring_charges` | — |
| 6 (Plan/Dashboard) | (artifact، مش tools) | — |
| 7 (Commit) | `knowledge__remember` | — |
| 8 (Follow-up) | `knowledge__recall_history`, `compare_spending_periods` | — |

---

## 🛡️ Error Handling

### لو tool رجّع error
- مش لازم تكسر الـ flow
- استخدم `knowledge__get_pending_questions` كـ fallback لجمع المعلومة يدوياً
- ولّد الـ Dashboard بالـ defaults + مساحة للمستخدم يدخل البيانات بنفسه

### لو الـ user رفض ربط Era
- اشتغل بـ form يدوي
- اعرض رسالة لطيفة:
  > "Era ممكن تفر بياناتك تلقائياً وتخلي الخطة أدق. لو حابب تفعلها بعدين، روح للـ Connectors في الإعدادات. حالياً، نشتغل بالأرقام اللي هتدخلها."

### لو الـ user وافق على Era بس الـ data فاضية
- اعرض على المستخدم الـ next steps:
  1. اربط حسابك البنكي في Era
  2. استنى يوم-يومين علشان البيانات تتجمع
  3. ارجع لنا

---

## ✨ Patterns ذكية

### Pattern 1: Smart Default من Era
لو المستخدم قال "عاوز أوفر لعربية"، استخدم Era data لاقتراح مبلغ معقول:
- اعرف الدخل الشهري من Era
- استخدم rule: "عربية معقولة ≤ 50% من الدخل السنوي"
- اقترح المبلغ كـ default في الـ Dashboard

### Pattern 2: المتابعة الذكية
لو المستخدم رجع بعد شهرين من الـ Commit:
- استدعِ `recall_history` للهدف
- استدعِ `compare_spending_periods` (شهرين قبل الهدف vs شهرين بعد)
- لو في category زادت بشكل غير متوقع → نبه المستخدم بلطف
- لو على المسار → احتفل معاه (1-2 جمل، مش طويل)

### Pattern 3: Cascading Goals
لو المستخدم عنده هدفين في فترات متداخلة:
- استدعِ `recall_history` لمعرفة الأهداف الموجودة
- اعرض في Tab 6 الخيار: "هل تستبدل الهدف الحالي ولا تضيف عليه؟"
- لو يضيف، قسّم الـ savings الشهرية على الهدفين بنسبة prioritization
