# Walkson Overseas Website — 使用与部署说明

英文外贸官网，纯静态（HTML/CSS/JS），无服务器、无数据库依赖。

## 页面结构
- `index.html` — 首页
- `products.html` — 产品目录（12 大类，265 款真实产品，带筛选）
- `about.html` — 关于我们
- `capabilities.html` — 生产能力与认证
- `contact.html` — 联系我们 + 询盘表单
- `404.html`、`robots.txt`、`sitemap.xml` — 辅助文件
- `assets/img/products/` — 265 张产品图（来自中国制造网店铺官方素材）
- `data/category-groups.json` — 产品数据源
- `build.py` — 网站生成脚本（改数据后重新生成页面）

## 本地预览
```bash
cd site
python3 -m http.server 8000
# 浏览器打开 http://localhost:8000
```

## 部署（推荐 Cloudflare Pages，免费）
1. 注册 Cloudflare 账号 → 添加域名 → 注册/接入域名
2. 进入 Workers & Pages → Create → Pages → Upload assets
3. 把 `dist/walkson-website/` 里所有文件拖拽上传
4. 绑定自定义域名（如 walksonmachinery.com），自动开启 HTTPS

## 需要修改的地方
- `build.py` 顶部 `EMAIL` / `SITE` / `PHONE` 三个变量改成客户确认后的真实信息
- 修改后运行 `python3 build.py` 重新生成页面

## 已内置的 SEO / AI 优化
- Organization、Product ItemList、FAQPage 结构化数据（JSON-LD）
- 每页独立 title / description / canonical / OpenGraph
- sitemap.xml + robots.txt
