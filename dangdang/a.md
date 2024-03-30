# 逆向当当网登陆，并做各下单小测试
# 1.登陆, 抓包
![1694416071288.png](https://gitss.oss-cn-shenzhen.aliyuncs.com/md/1694416071288.png)

用request请求去请求这个网页，可以获取到数据

`bgImg` , `slideImg` , `token` , `heightRatio` , `y` , `encryptKey` 

这个请求有个加密参数`sign` 
![1694416582884.png](https://gitss.oss-cn-shenzhen.aliyuncs.com/md/1694416582884.png)

生成sign代码
```
   function G(t) {
            var e = {
                t: (new Date).getTime(),
                ct: "pc",
                permanent_id: A.a.get("__permanent_id"),
                requestId: z.state.requestId
            };
            e = Object.assign(e, t);
            var n = {};
            Object.keys(e).sort().map((function(t) {
                ("sign" != t && e[t] || 0 === e[t]) && (n[t] = e[t])
            }
            ));
            var a = N.a.stringify(n);
            return a = decodeURIComponent(a),
						// 将参数拼接成字符串
            console.log("str:", a),
            a = Y(a), 
						// md5加密
            console.log("md5:", a),
            console.log("rankey:", z.state.rankey),
            a = J(a, z.state.rankey),
						// aes加密
            console.log("sign:", a),
            e.sign = a,
            e
        }
```




