---
name: dashboard-expert
description: Guides the AI to create professional, interactive, and insightful data dashboards using Python. Use when the user asks to "visualize results," "create a dashboard," or "build an interactive tool" for their data.
---

When building interactive dashboards, follow this professional framework to ensure the output is not just a collection of charts, but a powerful decision-making tool.

### 1. Framework Selection and Architecture
Choose the right tool based on the project's requirements for speed, complexity, and scale.
- **Streamlit**: Default choice for fast, beautiful, and interactive data apps.
- **Dash**: Use for enterprise-grade, highly customized, or complex multi-page applications.
- **Plotly/Seaborn**: Use for generating the underlying interactive or static charts.

### 2. Strategic Layout and Visual Hierarchy
Structure the dashboard to guide the user's eye from high-level summaries to granular details.
- **The KPI Header**: Place Key Performance Indicators (KPIs) in large, clear cards at the very top.
- **The Filter Sidebar**: Group interactive controls (date pickers, dropdowns, sliders) in a sidebar or a top horizontal bar to keep the main area clean.
- **Main Content Area**: Use a grid layout to organize charts. Primary trends go on the left, comparisons on the right.
- **The Detail View**: Place raw data tables or deep-dive charts at the bottom.

### 3. Implementing Interactivity
Interactivity should be purposeful and enhance discovery without confusing the user.
- **Global State**: Ensure filters affect all relevant charts simultaneously.
- **Reactive Updates**: Use caching (e.g., `st.cache_data`) to ensure the UI remains responsive when filters change.
- **Tooltips and Hover Effects**: Configure Plotly charts to show precise values and metadata on hover.

### 4. Design for Insight (The "So What?" Factor)
A dashboard is successful only if it provides actionable insights.
- **Benchmarking**: Don't just show a number; show it relative to a goal, a previous month, or an average.
- **Contextual Annotations**: Add text or markers to explain significant spikes or drops in the data.
- **Color Strategy**: Use color to convey meaning (e.g., a sequential palette for magnitude, a diverging palette for positive/negative deviations).

### 5. Technical Implementation Checklist
- **Data Efficiency**: Load data in Parquet format or use `pd.read_csv(chunksize=...)` for large files.
- **Responsive Design**: Ensure the dashboard scales gracefully across different screen sizes.
- **Documentation**: Include a "How to use" section or tooltips explaining what each metric represents.

### Example Workflow (Streamlit + Plotly)
1. **Import**: `import streamlit as st`, `import plotly.express as px`.
2. **Data**: Load and cache the dataset.
3. **Sidebar**: Create filters (e.g., `st.sidebar.multiselect`).
4. **KPIs**: Display key numbers using `st.metric`.
5. **Charts**: Create interactive Plotly charts based on filtered data and display via `st.plotly_chart`.
6. **Table**: Show a searchable dataframe using `st.dataframe`.
