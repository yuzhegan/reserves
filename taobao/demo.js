window=this;navigator = {};//如果需要用到浏览器协议头，请在<加载代码> 按钮 右侧选择 navigator.js

var M = function(e, t, n) {
    "use strict";
    var r;
    function o(e, t, n) {
        null != e && ("number" == typeof e ? this.fromNumber(e, t, n) : null == t && "string" != typeof e ? this.fromString(e, 256) : this.fromString(e, t))
    }
    function i() {
        return new o(null)
    }
    // Object.defineProperty(t, "__esModule", {
    //     value: !0
    // }),
    // t.default = void 0,
    // n(76139),
    // n(44321),
    // n(96780),
    "Microsoft Internet Explorer" == navigator.appName ? (o.prototype.am = function(e, t, n, r, o, i) {
        for (var a = 32767 & t, u = t >> 15; --i >= 0; ) {
            var c = 32767 & this[e]
              , s = this[e++] >> 15
              , l = u * c + s * a;
            o = ((c = a * c + ((32767 & l) << 15) + n[r] + (1073741823 & o)) >>> 30) + (l >>> 15) + u * s + (o >>> 30),
            n[r++] = 1073741823 & c
        }
        return o
    }
    ,
    r = 30) : "Netscape" != navigator.appName ? (o.prototype.am = function(e, t, n, r, o, i) {
        for (; --i >= 0; ) {
            var a = t * this[e++] + n[r] + o;
            o = Math.floor(a / 67108864),
            n[r++] = 67108863 & a
        }
        return o
    }
    ,
    r = 26) : (o.prototype.am = function(e, t, n, r, o, i) {
        for (var a = 16383 & t, u = t >> 14; --i >= 0; ) {
            var c = 16383 & this[e]
              , s = this[e++] >> 14
              , l = u * c + s * a;
            o = ((c = a * c + ((16383 & l) << 14) + n[r] + o) >> 28) + (l >> 14) + u * s,
            n[r++] = 268435455 & c
        }
        return o
    }
    ,
    r = 28),
    o.prototype.DB = r,
    o.prototype.DM = (1 << r) - 1,
    o.prototype.DV = 1 << r,
    o.prototype.FV = Math.pow(2, 52),
    o.prototype.F1 = 52 - r,
    o.prototype.F2 = 2 * r - 52;
    var a, u, c = "0123456789abcdefghijklmnopqrstuvwxyz", s = new Array;
    for (a = "0".charCodeAt(0),
    u = 0; u <= 9; ++u)
        s[a++] = u;
    for (a = "a".charCodeAt(0),
    u = 10; u < 36; ++u)
        s[a++] = u;
    for (a = "A".charCodeAt(0),
    u = 10; u < 36; ++u)
        s[a++] = u;
    function l(e) {
        return c.charAt(e)
    }
    function f(e, t) {
        var n = s[e.charCodeAt(t)];
        return null == n ? -1 : n
    }
    function d(e) {
        var t = i();
        return t.fromInt(e),
        t
    }
    function p(e) {
        var t, n = 1;
        return 0 != (t = e >>> 16) && (e = t,
        n += 16),
        0 != (t = e >> 8) && (e = t,
        n += 8),
        0 != (t = e >> 4) && (e = t,
        n += 4),
        0 != (t = e >> 2) && (e = t,
        n += 2),
        0 != (t = e >> 1) && (e = t,
        n += 1),
        n
    }
    function h(e) {
        this.m = e
    }
    function g(e) {
        this.m = e,
        this.mp = e.invDigit(),
        this.mpl = 32767 & this.mp,
        this.mph = this.mp >> 15,
        this.um = (1 << e.DB - 15) - 1,
        this.mt2 = 2 * e.t
    }
    function v() {
        this.i = 0,
        this.j = 0,
        this.S = new Array
    }
    h.prototype.convert = function(e) {
        return e.s < 0 || e.compareTo(this.m) >= 0 ? e.mod(this.m) : e
    }
    ,
    h.prototype.revert = function(e) {
        return e
    }
    ,
    h.prototype.reduce = function(e) {
        e.divRemTo(this.m, null, e)
    }
    ,
    h.prototype.mulTo = function(e, t, n) {
        e.multiplyTo(t, n),
        this.reduce(n)
    }
    ,
    h.prototype.sqrTo = function(e, t) {
        e.squareTo(t),
        this.reduce(t)
    }
    ,
    g.prototype.convert = function(e) {
        var t = i();
        return e.abs().dlShiftTo(this.m.t, t),
        t.divRemTo(this.m, null, t),
        e.s < 0 && t.compareTo(o.ZERO) > 0 && this.m.subTo(t, t),
        t
    }
    ,
    g.prototype.revert = function(e) {
        var t = i();
        return e.copyTo(t),
        this.reduce(t),
        t
    }
    ,
    g.prototype.reduce = function(e) {
        for (; e.t <= this.mt2; )
            e[e.t++] = 0;
        for (var t = 0; t < this.m.t; ++t) {
            var n = 32767 & e[t]
              , r = n * this.mpl + ((n * this.mph + (e[t] >> 15) * this.mpl & this.um) << 15) & e.DM;
            for (e[n = t + this.m.t] += this.m.am(0, r, e, t, 0, this.m.t); e[n] >= e.DV; )
                e[n] -= e.DV,
                e[++n]++
        }
        e.clamp(),
        e.drShiftTo(this.m.t, e),
        e.compareTo(this.m) >= 0 && e.subTo(this.m, e)
    }
    ,
    g.prototype.mulTo = function(e, t, n) {
        e.multiplyTo(t, n),
        this.reduce(n)
    }
    ,
    g.prototype.sqrTo = function(e, t) {
        e.squareTo(t),
        this.reduce(t)
    }
    ,
    o.prototype.copyTo = function(e) {
        for (var t = this.t - 1; t >= 0; --t)
            e[t] = this[t];
        e.t = this.t,
        e.s = this.s
    }
    ,
    o.prototype.fromInt = function(e) {
        this.t = 1,
        this.s = e < 0 ? -1 : 0,
        e > 0 ? this[0] = e : e < -1 ? this[0] = e + this.DV : this.t = 0
    }
    ,
    o.prototype.fromString = function(e, t) {
        var n;
        if (16 == t)
            n = 4;
        else if (8 == t)
            n = 3;
        else if (256 == t)
            n = 8;
        else if (2 == t)
            n = 1;
        else if (32 == t)
            n = 5;
        else {
            if (4 != t)
                return void this.fromRadix(e, t);
            n = 2
        }
        this.t = 0,
        this.s = 0;
        for (var r = e.length, i = !1, a = 0; --r >= 0; ) {
            var u = 8 == n ? 255 & e[r] : f(e, r);
            u < 0 ? "-" == e.charAt(r) && (i = !0) : (i = !1,
            0 == a ? this[this.t++] = u : a + n > this.DB ? (this[this.t - 1] |= (u & (1 << this.DB - a) - 1) << a,
            this[this.t++] = u >> this.DB - a) : this[this.t - 1] |= u << a,
            (a += n) >= this.DB && (a -= this.DB))
        }
        8 == n && 0 != (128 & e[0]) && (this.s = -1,
        a > 0 && (this[this.t - 1] |= (1 << this.DB - a) - 1 << a)),
        this.clamp(),
        i && o.ZERO.subTo(this, this)
    }
    ,
    o.prototype.clamp = function() {
        for (var e = this.s & this.DM; this.t > 0 && this[this.t - 1] == e; )
            --this.t
    }
    ,
    o.prototype.dlShiftTo = function(e, t) {
        var n;
        for (n = this.t - 1; n >= 0; --n)
            t[n + e] = this[n];
        for (n = e - 1; n >= 0; --n)
            t[n] = 0;
        t.t = this.t + e,
        t.s = this.s
    }
    ,
    o.prototype.drShiftTo = function(e, t) {
        for (var n = e; n < this.t; ++n)
            t[n - e] = this[n];
        t.t = Math.max(this.t - e, 0),
        t.s = this.s
    }
    ,
    o.prototype.lShiftTo = function(e, t) {
        var n, r = e % this.DB, o = this.DB - r, i = (1 << o) - 1, a = Math.floor(e / this.DB), u = this.s << r & this.DM;
        for (n = this.t - 1; n >= 0; --n)
            t[n + a + 1] = this[n] >> o | u,
            u = (this[n] & i) << r;
        for (n = a - 1; n >= 0; --n)
            t[n] = 0;
        t[a] = u,
        t.t = this.t + a + 1,
        t.s = this.s,
        t.clamp()
    }
    ,
    o.prototype.rShiftTo = function(e, t) {
        t.s = this.s;
        var n = Math.floor(e / this.DB);
        if (n >= this.t)
            t.t = 0;
        else {
            var r = e % this.DB
              , o = this.DB - r
              , i = (1 << r) - 1;
            t[0] = this[n] >> r;
            for (var a = n + 1; a < this.t; ++a)
                t[a - n - 1] |= (this[a] & i) << o,
                t[a - n] = this[a] >> r;
            r > 0 && (t[this.t - n - 1] |= (this.s & i) << o),
            t.t = this.t - n,
            t.clamp()
        }
    }
    ,
    o.prototype.subTo = function(e, t) {
        for (var n = 0, r = 0, o = Math.min(e.t, this.t); n < o; )
            r += this[n] - e[n],
            t[n++] = r & this.DM,
            r >>= this.DB;
        if (e.t < this.t) {
            for (r -= e.s; n < this.t; )
                r += this[n],
                t[n++] = r & this.DM,
                r >>= this.DB;
            r += this.s
        } else {
            for (r += this.s; n < e.t; )
                r -= e[n],
                t[n++] = r & this.DM,
                r >>= this.DB;
            r -= e.s
        }
        t.s = r < 0 ? -1 : 0,
        r < -1 ? t[n++] = this.DV + r : r > 0 && (t[n++] = r),
        t.t = n,
        t.clamp()
    }
    ,
    o.prototype.multiplyTo = function(e, t) {
        var n = this.abs()
          , r = e.abs()
          , i = n.t;
        for (t.t = i + r.t; --i >= 0; )
            t[i] = 0;
        for (i = 0; i < r.t; ++i)
            t[i + n.t] = n.am(0, r[i], t, i, 0, n.t);
        t.s = 0,
        t.clamp(),
        this.s != e.s && o.ZERO.subTo(t, t)
    }
    ,
    o.prototype.squareTo = function(e) {
        for (var t = this.abs(), n = e.t = 2 * t.t; --n >= 0; )
            e[n] = 0;
        for (n = 0; n < t.t - 1; ++n) {
            var r = t.am(n, t[n], e, 2 * n, 0, 1);
            (e[n + t.t] += t.am(n + 1, 2 * t[n], e, 2 * n + 1, r, t.t - n - 1)) >= t.DV && (e[n + t.t] -= t.DV,
            e[n + t.t + 1] = 1)
        }
        e.t > 0 && (e[e.t - 1] += t.am(n, t[n], e, 2 * n, 0, 1)),
        e.s = 0,
        e.clamp()
    }
    ,
    o.prototype.divRemTo = function(e, t, n) {
        var r = e.abs();
        if (!(r.t <= 0)) {
            var a = this.abs();
            if (a.t < r.t)
                return null != t && t.fromInt(0),
                void (null != n && this.copyTo(n));
            null == n && (n = i());
            var u = i()
              , c = this.s
              , s = e.s
              , l = this.DB - p(r[r.t - 1]);
            l > 0 ? (r.lShiftTo(l, u),
            a.lShiftTo(l, n)) : (r.copyTo(u),
            a.copyTo(n));
            var f = u.t
              , d = u[f - 1];
            if (0 != d) {
                var h = d * (1 << this.F1) + (f > 1 ? u[f - 2] >> this.F2 : 0)
                  , g = this.FV / h
                  , v = (1 << this.F1) / h
                  , y = 1 << this.F2
                  , m = n.t
                  , b = m - f
                  , w = null == t ? i() : t;
                for (u.dlShiftTo(b, w),
                n.compareTo(w) >= 0 && (n[n.t++] = 1,
                n.subTo(w, n)),
                o.ONE.dlShiftTo(f, w),
                w.subTo(u, u); u.t < f; )
                    u[u.t++] = 0;
                for (; --b >= 0; ) {
                    var M = n[--m] == d ? this.DM : Math.floor(n[m] * g + (n[m - 1] + y) * v);
                    if ((n[m] += u.am(0, M, n, b, 0, f)) < M)
                        for (u.dlShiftTo(b, w),
                        n.subTo(w, n); n[m] < --M; )
                            n.subTo(w, n)
                }
                null != t && (n.drShiftTo(f, t),
                c != s && o.ZERO.subTo(t, t)),
                n.t = f,
                n.clamp(),
                l > 0 && n.rShiftTo(l, n),
                c < 0 && o.ZERO.subTo(n, n)
            }
        }
    }
    ,
    o.prototype.invDigit = function() {
        if (this.t < 1)
            return 0;
        var e = this[0];
        if (0 == (1 & e))
            return 0;
        var t = 3 & e;
        return (t = (t = (t = (t = t * (2 - (15 & e) * t) & 15) * (2 - (255 & e) * t) & 255) * (2 - ((65535 & e) * t & 65535)) & 65535) * (2 - e * t % this.DV) % this.DV) > 0 ? this.DV - t : -t
    }
    ,
    o.prototype.isEven = function() {
        return 0 == (this.t > 0 ? 1 & this[0] : this.s)
    }
    ,
    o.prototype.exp = function(e, t) {
        if (e > 4294967295 || e < 1)
            return o.ONE;
        var n = i()
          , r = i()
          , a = t.convert(this)
          , u = p(e) - 1;
        for (a.copyTo(n); --u >= 0; )
            if (t.sqrTo(n, r),
            (e & 1 << u) > 0)
                t.mulTo(r, a, n);
            else {
                var c = n;
                n = r,
                r = c
            }
        return t.revert(n)
    }
    ,
    o.prototype.toString = function(e) {
        if (this.s < 0)
            return "-" + this.negate().toString(e);
        var t;
        if (16 == e)
            t = 4;
        else if (8 == e)
            t = 3;
        else if (2 == e)
            t = 1;
        else if (32 == e)
            t = 5;
        else {
            if (4 != e)
                return this.toRadix(e);
            t = 2
        }
        var n, r = (1 << t) - 1, o = !1, i = "", a = this.t, u = this.DB - a * this.DB % t;
        if (a-- > 0)
            for (u < this.DB && (n = this[a] >> u) > 0 && (o = !0,
            i = l(n)); a >= 0; )
                u < t ? (n = (this[a] & (1 << u) - 1) << t - u,
                n |= this[--a] >> (u += this.DB - t)) : (n = this[a] >> (u -= t) & r,
                u <= 0 && (u += this.DB,
                --a)),
                n > 0 && (o = !0),
                o && (i += l(n));
        return o ? i : "0"
    }
    ,
    o.prototype.negate = function() {
        var e = i();
        return o.ZERO.subTo(this, e),
        e
    }
    ,
    o.prototype.abs = function() {
        return this.s < 0 ? this.negate() : this
    }
    ,
    o.prototype.compareTo = function(e) {
        var t = this.s - e.s;
        if (0 != t)
            return t;
        var n = this.t;
        if (0 != (t = n - e.t))
            return this.s < 0 ? -t : t;
        for (; --n >= 0; )
            if (0 != (t = this[n] - e[n]))
                return t;
        return 0
    }
    ,
    o.prototype.bitLength = function() {
        return this.t <= 0 ? 0 : this.DB * (this.t - 1) + p(this[this.t - 1] ^ this.s & this.DM)
    }
    ,
    o.prototype.mod = function(e) {
        var t = i();
        return this.abs().divRemTo(e, null, t),
        this.s < 0 && t.compareTo(o.ZERO) > 0 && e.subTo(t, t),
        t
    }
    ,
    o.prototype.modPowInt = function(e, t) {
        var n;
        return n = e < 256 || t.isEven() ? new h(t) : new g(t),
        this.exp(e, n)
    }
    ,
    o.ZERO = d(0),
    o.ONE = d(1),
    v.prototype.init = function(e) {
        var t, n, r;
        for (t = 0; t < 256; ++t)
            this.S[t] = t;
        for (n = 0,
        t = 0; t < 256; ++t)
            n = n + this.S[t] + e[t % e.length] & 255,
            r = this.S[t],
            this.S[t] = this.S[n],
            this.S[n] = r;
        this.i = 0,
        this.j = 0
    }
    ,
    v.prototype.next = function() {
        var e;
        return this.i = this.i + 1 & 255,
        this.j = this.j + this.S[this.i] & 255,
        e = this.S[this.i],
        this.S[this.i] = this.S[this.j],
        this.S[this.j] = e,
        this.S[e + this.S[this.i] & 255]
    }
    ;
    var y, m, b, w = 256;
    function M() {
        !function(e) {
            m[b++] ^= 255 & e,
            m[b++] ^= e >> 8 & 255,
            m[b++] ^= e >> 16 & 255,
            m[b++] ^= e >> 24 & 255,
            b >= w && (b -= w)
        }((new Date).getTime())
    }
    if (null == m) {
        var S;
        if (m = new Array,
        b = 0,
        window.crypto && window.crypto.getRandomValues) {
            var T = new Uint8Array(32);
            for (window.crypto.getRandomValues(T),
            S = 0; S < 32; ++S)
                m[b++] = T[S]
        }
        if ("Netscape" == navigator.appName && navigator.appVersion < "5" && window.crypto && window.crypto.random) {
            var _ = window.crypto.random(32);
            for (S = 0; S < _.length; ++S)
                m[b++] = 255 & _.charCodeAt(S)
        }
        for (; b < w; )
            S = Math.floor(65536 * Math.random()),
            m[b++] = S >>> 8,
            m[b++] = 255 & S;
        b = 0,
        M()
    }
    function N() {
        if (null == y) {
            for (M(),
            (y = new v).init(m),
            b = 0; b < m.length; ++b)
                m[b] = 0;
            b = 0
        }
        return y.next()
    }
    function x() {}
    function C() {
        this.n = null,
        this.e = 0,
        this.d = null,
        this.p = null,
        this.q = null,
        this.dmp1 = null,
        this.dmq1 = null,
        this.coeff = null
    }
    x.prototype.nextBytes = function(e) {
        var t;
        for (t = 0; t < e.length; ++t)
            e[t] = N()
    }
    ,
    C.prototype.doPublic = function(e) {
        return e.modPowInt(this.e, this.n)
    }
    ,
    C.prototype.setPublic = function(e, t) {
        null != e && null != t && e.length > 0 && t.length > 0 ? (this.n = function(e, t) {
            return new o(e,16)
        }(e),
        this.e = parseInt(t, 16)) : alert("Invalid RSA public key")
    }
    ,
    C.prototype.encrypt = function(e) {
        var t = function(e, t) {
            if (t < e.length + 11)
                return alert("Message too long for RSA"),
                null;
            for (var n = new Array, r = e.length - 1; r >= 0 && t > 0; ) {
                var i = e.charCodeAt(r--);
                i < 128 ? n[--t] = i : i > 127 && i < 2048 ? (n[--t] = 63 & i | 128,
                n[--t] = i >> 6 | 192) : (n[--t] = 63 & i | 128,
                n[--t] = i >> 6 & 63 | 128,
                n[--t] = i >> 12 | 224)
            }
            n[--t] = 0;
            for (var a = new x, u = new Array; t > 2; ) {
                for (u[0] = 0; 0 == u[0]; )
                    a.nextBytes(u);
                n[--t] = u[0]
            }
            return n[--t] = 2,
            n[--t] = 0,
            new o(n)
        }(e, this.n.bitLength() + 7 >> 3);
        if (null == t)
            return null;
        var n = this.doPublic(t);
        if (null == n)
            return null;
        var r = n.toString(16);
        return 0 == (1 & r.length) ? r : "0" + r
    }
    ;
    var k = C;
    // t.default = k
    return C

}

var rsaModulus = 'd3bcef1f00424f3261c89323fa8cdfa12bbac400d9fe8bb627e8d27a44bd5d59dce559135d678a8143beb5b8d7056c4e1f89c4e1f152470625b7b41944a97f02da6f605a49a93ec6eb9cbaf2e7ac2b26a354ce69eb265953d2c29e395d6d8c1cdb688978551aa0f7521f290035fad381178da0bea8f9e6adce39020f513133fb'
var rsaExponent = '10001'


function getpwd(e) {
                        var t = new M;
                        return t.prototype.setPublic(rsaModulus, rsaExponent),
                        t.prototype.encrypt(e)
                    }
// console.log(getpwd('123456'))
