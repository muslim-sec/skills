---
name: brand-pdf-generator
description: Generates highly stylized, brand-aligned PDFs using HTML/Tailwind CSS and headless browser rendering to preserve exact typography, layout, and colors.
---

# Brand PDF Generator

**Role:** Editorial Designer & Print Developer
**Objective:** Generate flawless, multi-page PDFs that strictly adhere to a brand identity without looking like a generic web page or Word document.

## The Architecture: Template-Driven HTML-to-PDF
Standard markdown-to-PDF tools destroy custom branding. To achieve 10/10 visual quality, you must write an HTML/Tailwind template and render it using a headless browser (Puppeteer).

## Workflow

### 1. Extract Brand Identity & Scaffold Project
- Analyze the reference document for exact HEX colors, typography (e.g., Cairo/Tajawal for Arabic), and layout structures.
- **Dependency Check:** Before writing the template, ensure Puppeteer is installed in the scratch directory:
  ```bash
  npm init -y && npm install puppeteer
  ```

### 2. Write the HTML/Tailwind Template
Create `template.html`. 
- Include the Tailwind CDN and Google Fonts.
- Define custom colors in the Tailwind config block.
- For RTL text, set `<html dir="rtl">`.
- **Handling Overflow:** Do NOT use fixed heights for content wrappers. Use `break-inside-avoid` on critical elements (like tables or checklists) so they jump cleanly to the next page instead of splitting in half.

```html
<!DOCTYPE html>
<html dir="rtl">
<head>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
  <script>
    tailwind.config = { theme: { extend: { colors: { brandYellow: '#FFCC00', brandBlue: '#0055FF' } } } }
  </script>
  <style>
    body { font-family: 'Cairo', sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    /* Force page breaks in printing */
    .page-break { page-break-after: always; }
    .avoid-break { break-inside: avoid; }
  </style>
</head>
<body class="bg-gray-50 text-gray-900">
  <!-- Content goes here -->
</body>
</html>
```

### 3. The Perfect Render Script
Never rely on CSS `@page` for page numbers. Use Puppeteer's native headers and footers. The most critical step is `document.fonts.ready` — without it, custom fonts will silently fail to render in the PDF.

Create `render.js`:
```javascript
const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // 1. Load the HTML template
  await page.goto(`file://${path.resolve(__dirname, 'template.html')}`, { waitUntil: 'networkidle0' });
  
  // 2. CRITICAL: Wait for all web fonts to fully render
  await page.evaluateHandle('document.fonts.ready');

  // 3. Render to PDF with dynamic page numbering
  await page.pdf({
    path: 'output.pdf',
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>', // Empty header
    footerTemplate: `
      <div style="width: 100%; font-size: 10px; font-family: sans-serif; padding: 0 20px; display: flex; justify-content: space-between; color: #666;">
        <span>My Brand Identity</span>
        <span class="pageNumber"></span>
      </div>
    `,
    margin: { top: '20mm', bottom: '20mm', left: '10mm', right: '10mm' }
  });

  await browser.close();
  console.log("PDF successfully generated at output.pdf");
})();
```

### 4. Execute and Verify
Run `node render.js` and verify the output. If the text clips or overflows, adjust the CSS padding or `break-inside-avoid` rules and re-render.
