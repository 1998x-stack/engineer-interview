# Crawler 故障排查 Checklist

1. **Queue**：oldest age、depth、consumer lag 是否异常？
2. **Infrastructure**：CPU、RSS、FD、DNS、连接池是否饱和？
3. **HTTP**：2xx/3xx/4xx/5xx 分布、429/503、redirect 是否突变？
4. **Remote latency**：TTFB 是否上升？只发生在特定 host 吗？
5. **Content**：response size、content-type、登录页/错误模板比例？
6. **Parser**：items/page、required-field completeness、schema error？
7. **Browser**：fallback rate、OOM、navigation timeout、JS error？
8. **Storage**：写入 p95、失败率、backpressure？
9. **Policy**：robots、预算、授权、配置是否有发布变更？
10. **Version**：spider/parser/browser/library 版本是否刚升级？
