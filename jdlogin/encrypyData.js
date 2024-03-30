let gyx;
!function(t, e) {
	if ("object" == typeof exports && "object" == typeof module)
		module.exports = e();
	else if ("function" == typeof define && define.amd)
		define([], e);
	else {
		var r, i = e();
		for (r in i)
			("object" == typeof exports ? exports : t)[r] = i[r]
	}
}(this, (function() {
	var t = {
		77: function(t, e) {
			(function() {
				function e(t, e, r) {
					null != t && ("number" == typeof t ? this.fromNumber(t, e, r) : null == e && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, e))
				}
				function r() {
					return new e(null)
				}
				var i = (i = "undefined" != typeof navigator) && "Microsoft Internet Explorer" == navigator.appName ? (e.prototype.am = function(t, e, r, i, n, o) {
					for (var s = 32767 & e, h = e >> 15; 0 <= --o;) {
						var u = 32767 & this[t]
							, a = this[t++] >> 15
							, c = h * u + a * s;
						n = ((u = s * u + ((32767 & c) << 15) + r[i] + (1073741823 & n)) >>> 30) + (c >>> 15) + h * a + (n >>> 30),
							r[i++] = 1073741823 & u
					}
					return n
				}
					,
					30) : i && "Netscape" != navigator.appName ? (e.prototype.am = function(t, e, r, i, n, o) {
						for (; 0 <= --o;) {
							var s = e * this[t++] + r[i] + n;
							n = Math.floor(s / 67108864),
								r[i++] = 67108863 & s
						}
						return n
					}
						,
						26) : (e.prototype.am = function(t, e, r, i, n, o) {
							for (var s = 16383 & e, h = e >> 14; 0 <= --o;) {
								var u = 16383 & this[t]
									, a = this[t++] >> 14
									, c = h * u + a * s;
								n = ((u = s * u + ((16383 & c) << 14) + r[i] + n) >> 28) + (c >> 14) + h * a,
									r[i++] = 268435455 & u
							}
							return n
						}
							,
							28);
				e.prototype.DB = i,
					e.prototype.DM = (1 << i) - 1,
					e.prototype.DV = 1 << i,
					e.prototype.FV = Math.pow(2, 52),
					e.prototype.F1 = 52 - i,
					e.prototype.F2 = 2 * i - 52;
				for (var n = new Array, o = "0".charCodeAt(0), s = 0; s <= 9; ++s)
					n[o++] = s;
				for (o = "a".charCodeAt(0),
					s = 10; s < 36; ++s)
					n[o++] = s;
				for (o = "A".charCodeAt(0),
					s = 10; s < 36; ++s)
					n[o++] = s;
				function h(t) {
					return "0123456789abcdefghijklmnopqrstuvwxyz".charAt(t)
				}
				function u(t, e) {
					return null == (e = n[t.charCodeAt(e)]) ? -1 : e
				}
				function a(t) {
					var e = r();
					return e.fromInt(t),
						e
				}
				function c(t) {
					var e, r = 1;
					return 0 != (e = t >>> 16) && (t = e,
						r += 16),
						0 != (e = t >> 8) && (t = e,
							r += 8),
						0 != (e = t >> 4) && (t = e,
							r += 4),
						0 != (e = t >> 2) && (t = e,
							r += 2),
						0 != (e = t >> 1) && (t = e,
							r += 1),
						r
				}
				function f(t) {
					this.m = t
				}
				function p(t) {
					this.m = t,
						this.mp = t.invDigit(),
						this.mpl = 32767 & this.mp,
						this.mph = this.mp >> 15,
						this.um = (1 << t.DB - 15) - 1,
						this.mt2 = 2 * t.t
				}
				function l(t, e) {
					return t & e
				}
				function y(t, e) {
					return t | e
				}
				function d(t, e) {
					return t ^ e
				}
				function m(t, e) {
					return t & ~e
				}
				function v() { }
				function g(t) {
					return t
				}
				function b(t) {
					this.r2 = r(),
						this.q3 = r(),
						e.ONE.dlShiftTo(2 * t.t, this.r2),
						this.mu = this.r2.divide(t),
						this.m = t
				}
				f.prototype.convert = function(t) {
					return t.s < 0 || 0 <= t.compareTo(this.m) ? t.mod(this.m) : t
				}
					,
					f.prototype.revert = function(t) {
						return t
					}
					,
					f.prototype.reduce = function(t) {
						t.divRemTo(this.m, null, t)
					}
					,
					f.prototype.mulTo = function(t, e, r) {
						t.multiplyTo(e, r),
							this.reduce(r)
					}
					,
					f.prototype.sqrTo = function(t, e) {
						t.squareTo(e),
							this.reduce(e)
					}
					,
					p.prototype.convert = function(t) {
						var i = r();
						return t.abs().dlShiftTo(this.m.t, i),
							i.divRemTo(this.m, null, i),
							t.s < 0 && 0 < i.compareTo(e.ZERO) && this.m.subTo(i, i),
							i
					}
					,
					p.prototype.revert = function(t) {
						var e = r();
						return t.copyTo(e),
							this.reduce(e),
							e
					}
					,
					p.prototype.reduce = function(t) {
						for (; t.t <= this.mt2;)
							t[t.t++] = 0;
						for (var e = 0; e < this.m.t; ++e) {
							var r = 32767 & t[e]
								, i = r * this.mpl + ((r * this.mph + (t[e] >> 15) * this.mpl & this.um) << 15) & t.DM;
							for (t[r = e + this.m.t] += this.m.am(0, i, t, e, 0, this.m.t); t[r] >= t.DV;)
								t[r] -= t.DV,
									t[++r]++
						}
						t.clamp(),
							t.drShiftTo(this.m.t, t),
							0 <= t.compareTo(this.m) && t.subTo(this.m, t)
					}
					,
					p.prototype.mulTo = function(t, e, r) {
						t.multiplyTo(e, r),
							this.reduce(r)
					}
					,
					p.prototype.sqrTo = function(t, e) {
						t.squareTo(e),
							this.reduce(e)
					}
					,
					e.prototype.copyTo = function(t) {
						for (var e = this.t - 1; 0 <= e; --e)
							t[e] = this[e];
						t.t = this.t,
							t.s = this.s
					}
					,
					e.prototype.fromInt = function(t) {
						this.t = 1,
							this.s = t < 0 ? -1 : 0,
							0 < t ? this[0] = t : t < -1 ? this[0] = t + this.DV : this.t = 0
					}
					,
					e.prototype.fromString = function(t, r) {
						var i;
						if (16 == r)
							i = 4;
						else if (8 == r)
							i = 3;
						else if (256 == r)
							i = 8;
						else if (2 == r)
							i = 1;
						else if (32 == r)
							i = 5;
						else {
							if (4 != r)
								return void this.fromRadix(t, r);
							i = 2
						}
						this.t = 0,
							this.s = 0;
						for (var n = t.length, o = !1, s = 0; 0 <= --n;) {
							var h = 8 == i ? 255 & t[n] : u(t, n);
							h < 0 ? "-" == t.charAt(n) && (o = !0) : (o = !1,
								0 == s ? this[this.t++] = h : s + i > this.DB ? (this[this.t - 1] |= (h & (1 << this.DB - s) - 1) << s,
									this[this.t++] = h >> this.DB - s) : this[this.t - 1] |= h << s,
								(s += i) >= this.DB && (s -= this.DB))
						}
						8 == i && 0 != (128 & t[0]) && (this.s = -1,
							0 < s && (this[this.t - 1] |= (1 << this.DB - s) - 1 << s)),
							this.clamp(),
							o && e.ZERO.subTo(this, this)
					}
					,
					e.prototype.clamp = function() {
						for (var t = this.s & this.DM; 0 < this.t && this[this.t - 1] == t;)
							--this.t
					}
					,
					e.prototype.dlShiftTo = function(t, e) {
						for (var r = this.t - 1; 0 <= r; --r)
							e[r + t] = this[r];
						for (r = t - 1; 0 <= r; --r)
							e[r] = 0;
						e.t = this.t + t,
							e.s = this.s
					}
					,
					e.prototype.drShiftTo = function(t, e) {
						for (var r = t; r < this.t; ++r)
							e[r - t] = this[r];
						e.t = Math.max(this.t - t, 0),
							e.s = this.s
					}
					,
					e.prototype.lShiftTo = function(t, e) {
						for (var r = t % this.DB, i = this.DB - r, n = (1 << i) - 1, o = Math.floor(t / this.DB), s = this.s << r & this.DM, h = this.t - 1; 0 <= h; --h)
							e[h + o + 1] = this[h] >> i | s,
								s = (this[h] & n) << r;
						for (h = o - 1; 0 <= h; --h)
							e[h] = 0;
						e[o] = s,
							e.t = this.t + o + 1,
							e.s = this.s,
							e.clamp()
					}
					,
					e.prototype.rShiftTo = function(t, e) {
						e.s = this.s;
						var r = Math.floor(t / this.DB);
						if (r >= this.t)
							e.t = 0;
						else {
							var i = t % this.DB
								, n = this.DB - i
								, o = (1 << i) - 1;
							e[0] = this[r] >> i;
							for (var s = r + 1; s < this.t; ++s)
								e[s - r - 1] |= (this[s] & o) << n,
									e[s - r] = this[s] >> i;
							0 < i && (e[this.t - r - 1] |= (this.s & o) << n),
								e.t = this.t - r,
								e.clamp()
						}
					}
					,
					e.prototype.subTo = function(t, e) {
						for (var r = 0, i = 0, n = Math.min(t.t, this.t); r < n;)
							i += this[r] - t[r],
								e[r++] = i & this.DM,
								i >>= this.DB;
						if (t.t < this.t) {
							for (i -= t.s; r < this.t;)
								i += this[r],
									e[r++] = i & this.DM,
									i >>= this.DB;
							i += this.s
						} else {
							for (i += this.s; r < t.t;)
								i -= t[r],
									e[r++] = i & this.DM,
									i >>= this.DB;
							i -= t.s
						}
						e.s = i < 0 ? -1 : 0,
							i < -1 ? e[r++] = this.DV + i : 0 < i && (e[r++] = i),
							e.t = r,
							e.clamp()
					}
					,
					e.prototype.multiplyTo = function(t, r) {
						var i = this.abs()
							, n = t.abs()
							, o = i.t;
						for (r.t = o + n.t; 0 <= --o;)
							r[o] = 0;
						for (o = 0; o < n.t; ++o)
							r[o + i.t] = i.am(0, n[o], r, o, 0, i.t);
						r.s = 0,
							r.clamp(),
							this.s != t.s && e.ZERO.subTo(r, r)
					}
					,
					e.prototype.squareTo = function(t) {
						for (var e = this.abs(), r = t.t = 2 * e.t; 0 <= --r;)
							t[r] = 0;
						for (r = 0; r < e.t - 1; ++r) {
							var i = e.am(r, e[r], t, 2 * r, 0, 1);
							(t[r + e.t] += e.am(r + 1, 2 * e[r], t, 2 * r + 1, i, e.t - r - 1)) >= e.DV && (t[r + e.t] -= e.DV,
								t[r + e.t + 1] = 1)
						}
						0 < t.t && (t[t.t - 1] += e.am(r, e[r], t, 2 * r, 0, 1)),
							t.s = 0,
							t.clamp()
					}
					,
					e.prototype.divRemTo = function(t, i, n) {
						var o = t.abs();
						if (!(o.t <= 0)) {
							if ((p = this.abs()).t < o.t)
								return null != i && i.fromInt(0),
									void (null != n && this.copyTo(n));
							null == n && (n = r());
							var s = r()
								, h = this.s
								, u = t.s;
							0 < (t = this.DB - c(o[o.t - 1])) ? (o.lShiftTo(t, s),
								p.lShiftTo(t, n)) : (o.copyTo(s),
									p.copyTo(n));
							var a = s.t
								, f = s[a - 1];
							if (0 != f) {
								var p = f * (1 << this.F1) + (1 < a ? s[a - 2] >> this.F2 : 0)
									, l = this.FV / p
									, y = (1 << this.F1) / p
									, d = 1 << this.F2
									, m = n.t
									, v = m - a
									, g = null == i ? r() : i;
								for (s.dlShiftTo(v, g),
									0 <= n.compareTo(g) && (n[n.t++] = 1,
										n.subTo(g, n)),
									e.ONE.dlShiftTo(a, g),
									g.subTo(s, s); s.t < a;)
									s[s.t++] = 0;
								for (; 0 <= --v;) {
									var b = n[--m] == f ? this.DM : Math.floor(n[m] * l + (n[m - 1] + d) * y);
									if ((n[m] += s.am(0, b, n, v, 0, a)) < b)
										for (s.dlShiftTo(v, g),
											n.subTo(g, n); n[m] < --b;)
											n.subTo(g, n)
								}
								null != i && (n.drShiftTo(a, i),
									h != u && e.ZERO.subTo(i, i)),
									n.t = a,
									n.clamp(),
									0 < t && n.rShiftTo(t, n),
									h < 0 && e.ZERO.subTo(n, n)
							}
						}
					}
					,
					e.prototype.invDigit = function() {
						if (this.t < 1)
							return 0;
						var t = this[0];
						if (0 == (1 & t))
							return 0;
						var e = 3 & t;
						return 0 < (e = (e = (e = (e = e * (2 - (15 & t) * e) & 15) * (2 - (255 & t) * e) & 255) * (2 - ((65535 & t) * e & 65535)) & 65535) * (2 - t * e % this.DV) % this.DV) ? this.DV - e : -e
					}
					,
					e.prototype.isEven = function() {
						return 0 == (0 < this.t ? 1 & this[0] : this.s)
					}
					,
					e.prototype.exp = function(t, i) {
						if (4294967295 < t || t < 1)
							return e.ONE;
						var n, o = r(), s = r(), h = i.convert(this), u = c(t) - 1;
						for (h.copyTo(o); 0 <= --u;)
							i.sqrTo(o, s),
								0 < (t & 1 << u) ? i.mulTo(s, h, o) : (n = o,
									o = s,
									s = n);
						return i.revert(o)
					}
					,
					e.prototype.toString = function(t) {
						if (this.s < 0)
							return "-" + this.negate().toString(t);
						var e;
						if (16 == t)
							e = 4;
						else if (8 == t)
							e = 3;
						else if (2 == t)
							e = 1;
						else if (32 == t)
							e = 5;
						else {
							if (4 != t)
								return this.toRadix(t);
							e = 2
						}
						var r, i = (1 << e) - 1, n = !1, o = "", s = this.t, u = this.DB - s * this.DB % e;
						if (0 < s--)
							for (u < this.DB && 0 < (r = this[s] >> u) && (n = !0,
								o = h(r)); 0 <= s;)
								u < e ? (r = (this[s] & (1 << u) - 1) << e - u,
									r |= this[--s] >> (u += this.DB - e)) : (r = this[s] >> (u -= e) & i,
										u <= 0 && (u += this.DB,
											--s)),
									(n = 0 < r || n) && (o += h(r));
						return n ? o : "0"
					}
					,
					e.prototype.negate = function() {
						var t = r();
						return e.ZERO.subTo(this, t),
							t
					}
					,
					e.prototype.abs = function() {
						return this.s < 0 ? this.negate() : this
					}
					,
					e.prototype.compareTo = function(t) {
						var e = this.s - t.s;
						if (0 != e)
							return e;
						var r = this.t;
						if (0 != (e = r - t.t))
							return this.s < 0 ? -e : e;
						for (; 0 <= --r;)
							if (0 != (e = this[r] - t[r]))
								return e;
						return 0
					}
					,
					e.prototype.bitLength = function() {
						return this.t <= 0 ? 0 : this.DB * (this.t - 1) + c(this[this.t - 1] ^ this.s & this.DM)
					}
					,
					e.prototype.mod = function(t) {
						var i = r();
						return this.abs().divRemTo(t, null, i),
							this.s < 0 && 0 < i.compareTo(e.ZERO) && t.subTo(i, i),
							i
					}
					,
					e.prototype.modPowInt = function(t, e) {
						return e = new (t < 256 || e.isEven() ? f : p)(e),
							this.exp(t, e)
					}
					,
					e.ZERO = a(0),
					e.ONE = a(1),
					v.prototype.convert = g,
					v.prototype.revert = g,
					v.prototype.mulTo = function(t, e, r) {
						t.multiplyTo(e, r)
					}
					,
					v.prototype.sqrTo = function(t, e) {
						t.squareTo(e)
					}
					,
					b.prototype.convert = function(t) {
						if (t.s < 0 || t.t > 2 * this.m.t)
							return t.mod(this.m);
						if (t.compareTo(this.m) < 0)
							return t;
						var e = r();
						return t.copyTo(e),
							this.reduce(e),
							e
					}
					,
					b.prototype.revert = function(t) {
						return t
					}
					,
					b.prototype.reduce = function(t) {
						for (t.drShiftTo(this.m.t - 1, this.r2),
							t.t > this.m.t + 1 && (t.t = this.m.t + 1,
								t.clamp()),
							this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
							this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); t.compareTo(this.r2) < 0;)
							t.dAddOffset(1, this.m.t + 1);
						for (t.subTo(this.r2, t); 0 <= t.compareTo(this.m);)
							t.subTo(this.m, t)
					}
					,
					b.prototype.mulTo = function(t, e, r) {
						t.multiplyTo(e, r),
							this.reduce(r)
					}
					,
					b.prototype.sqrTo = function(t, e) {
						t.squareTo(e),
							this.reduce(e)
					}
					;
				var T, w = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997], F = (1 << 26) / w[w.length - 1];
				function S() {
					var t;
					t = (new Date).getTime(),
						x[B++] ^= 255 & t,
						x[B++] ^= t >> 8 & 255,
						x[B++] ^= t >> 16 & 255,
						x[B++] ^= t >> 24 & 255,
						O <= B && (B -= O)
				}
				e.prototype.chunkSize = function(t) {
					return Math.floor(Math.LN2 * this.DB / Math.log(t))
				}
					,
					e.prototype.toRadix = function(t) {
						if (null == t && (t = 10),
							0 == this.signum() || t < 2 || 36 < t)
							return "0";
						var e = this.chunkSize(t)
							, i = Math.pow(t, e)
							, n = a(i)
							, o = r()
							, s = r()
							, h = "";
						for (this.divRemTo(n, o, s); 0 < o.signum();)
							h = (i + s.intValue()).toString(t).substr(1) + h,
								o.divRemTo(n, o, s);
						return s.intValue().toString(t) + h
					}
					,
					e.prototype.fromRadix = function(t, r) {
						this.fromInt(0);
						for (var i = this.chunkSize(r = null == r ? 10 : r), n = Math.pow(r, i), o = !1, s = 0, h = 0, a = 0; a < t.length; ++a) {
							var c = u(t, a);
							c < 0 ? "-" == t.charAt(a) && 0 == this.signum() && (o = !0) : (h = r * h + c,
								++s >= i && (this.dMultiply(n),
									this.dAddOffset(h, 0),
									h = s = 0))
						}
						0 < s && (this.dMultiply(Math.pow(r, s)),
							this.dAddOffset(h, 0)),
							o && e.ZERO.subTo(this, this)
					}
					,
					e.prototype.fromNumber = function(t, r, i) {
						if ("number" == typeof r)
							if (t < 2)
								this.fromInt(1);
							else
								for (this.fromNumber(t, i),
									this.testBit(t - 1) || this.bitwiseTo(e.ONE.shiftLeft(t - 1), y, this),
									this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(r);)
									this.dAddOffset(2, 0),
										this.bitLength() > t && this.subTo(e.ONE.shiftLeft(t - 1), this);
						else {
							var n = new Array;
							i = 7 & t,
								n.length = 1 + (t >> 3),
								r.nextBytes(n),
								0 < i ? n[0] &= (1 << i) - 1 : n[0] = 0,
								this.fromString(n, 256)
						}
					}
					,
					e.prototype.bitwiseTo = function(t, e, r) {
						for (var i, n = Math.min(t.t, this.t), o = 0; o < n; ++o)
							r[o] = e(this[o], t[o]);
						if (t.t < this.t) {
							for (i = t.s & this.DM,
								o = n; o < this.t; ++o)
								r[o] = e(this[o], i);
							r.t = this.t
						} else {
							for (i = this.s & this.DM,
								o = n; o < t.t; ++o)
								r[o] = e(i, t[o]);
							r.t = t.t
						}
						r.s = e(this.s, t.s),
							r.clamp()
					}
					,
					e.prototype.changeBit = function(t, r) {
						return t = e.ONE.shiftLeft(t),
							this.bitwiseTo(t, r, t),
							t
					}
					,
					e.prototype.addTo = function(t, e) {
						for (var r = 0, i = 0, n = Math.min(t.t, this.t); r < n;)
							i += this[r] + t[r],
								e[r++] = i & this.DM,
								i >>= this.DB;
						if (t.t < this.t) {
							for (i += t.s; r < this.t;)
								i += this[r],
									e[r++] = i & this.DM,
									i >>= this.DB;
							i += this.s
						} else {
							for (i += this.s; r < t.t;)
								i += t[r],
									e[r++] = i & this.DM,
									i >>= this.DB;
							i += t.s
						}
						e.s = i < 0 ? -1 : 0,
							0 < i ? e[r++] = i : i < -1 && (e[r++] = this.DV + i),
							e.t = r,
							e.clamp()
					}
					,
					e.prototype.dMultiply = function(t) {
						this[this.t] = this.am(0, t - 1, this, 0, 0, this.t),
							++this.t,
							this.clamp()
					}
					,
					e.prototype.dAddOffset = function(t, e) {
						if (0 != t) {
							for (; this.t <= e;)
								this[this.t++] = 0;
							for (this[e] += t; this[e] >= this.DV;)
								this[e] -= this.DV,
									++e >= this.t && (this[this.t++] = 0),
									++this[e]
						}
					}
					,
					e.prototype.multiplyLowerTo = function(t, e, r) {
						var i, n = Math.min(this.t + t.t, e);
						for (r.s = 0,
							r.t = n; 0 < n;)
							r[--n] = 0;
						for (i = r.t - this.t; n < i; ++n)
							r[n + this.t] = this.am(0, t[n], r, n, 0, this.t);
						for (i = Math.min(t.t, e); n < i; ++n)
							this.am(0, t[n], r, n, 0, e - n);
						r.clamp()
					}
					,
					e.prototype.multiplyUpperTo = function(t, e, r) {
						var i = r.t = this.t + t.t - --e;
						for (r.s = 0; 0 <= --i;)
							r[i] = 0;
						for (i = Math.max(e - this.t, 0); i < t.t; ++i)
							r[this.t + i - e] = this.am(e - i, t[i], r, 0, 0, this.t + i - e);
						r.clamp(),
							r.drShiftTo(1, r)
					}
					,
					e.prototype.modInt = function(t) {
						if (t <= 0)
							return 0;
						var e = this.DV % t
							, r = this.s < 0 ? t - 1 : 0;
						if (0 < this.t)
							if (0 == e)
								r = this[0] % t;
							else
								for (var i = this.t - 1; 0 <= i; --i)
									r = (e * r + this[i]) % t;
						return r
					}
					,
					e.prototype.millerRabin = function(t) {
						var i = this.subtract(e.ONE)
							, n = i.getLowestSetBit();
						if (n <= 0)
							return !1;
						var o = i.shiftRight(n);
						w.length < (t = t + 1 >> 1) && (t = w.length);
						for (var s = r(), h = 0; h < t; ++h) {
							s.fromInt(w[Math.floor(Math.random() * w.length)]);
							var u = s.modPow(o, this);
							if (0 != u.compareTo(e.ONE) && 0 != u.compareTo(i)) {
								for (var a = 1; a++ < n && 0 != u.compareTo(i);)
									if (0 == (u = u.modPowInt(2, this)).compareTo(e.ONE))
										return !1;
								if (0 != u.compareTo(i))
									return !1
							}
						}
						return !0
					}
					,
					e.prototype.clone = function() {
						var t = r();
						return this.copyTo(t),
							t
					}
					,
					e.prototype.intValue = function() {
						if (this.s < 0) {
							if (1 == this.t)
								return this[0] - this.DV;
							if (0 == this.t)
								return -1
						} else {
							if (1 == this.t)
								return this[0];
							if (0 == this.t)
								return 0
						}
						return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
					}
					,
					e.prototype.byteValue = function() {
						return 0 == this.t ? this.s : this[0] << 24 >> 24
					}
					,
					e.prototype.shortValue = function() {
						return 0 == this.t ? this.s : this[0] << 16 >> 16
					}
					,
					e.prototype.signum = function() {
						return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
					}
					,
					e.prototype.toByteArray = function() {
						var t = this.t
							, e = new Array;
						e[0] = this.s;
						var r, i = this.DB - t * this.DB % 8, n = 0;
						if (0 < t--)
							for (i < this.DB && (r = this[t] >> i) != (this.s & this.DM) >> i && (e[n++] = r | this.s << this.DB - i); 0 <= t;)
								i < 8 ? (r = (this[t] & (1 << i) - 1) << 8 - i,
									r |= this[--t] >> (i += this.DB - 8)) : (r = this[t] >> (i -= 8) & 255,
										i <= 0 && (i += this.DB,
											--t)),
									0 != (128 & r) && (r |= -256),
									0 == n && (128 & this.s) != (128 & r) && ++n,
									(0 < n || r != this.s) && (e[n++] = r);
						return e
					}
					,
					e.prototype.equals = function(t) {
						return 0 == this.compareTo(t)
					}
					,
					e.prototype.min = function(t) {
						return this.compareTo(t) < 0 ? this : t
					}
					,
					e.prototype.max = function(t) {
						return 0 < this.compareTo(t) ? this : t
					}
					,
					e.prototype.and = function(t) {
						var e = r();
						return this.bitwiseTo(t, l, e),
							e
					}
					,
					e.prototype.or = function(t) {
						var e = r();
						return this.bitwiseTo(t, y, e),
							e
					}
					,
					e.prototype.xor = function(t) {
						var e = r();
						return this.bitwiseTo(t, d, e),
							e
					}
					,
					e.prototype.andNot = function(t) {
						var e = r();
						return this.bitwiseTo(t, m, e),
							e
					}
					,
					e.prototype.not = function() {
						for (var t = r(), e = 0; e < this.t; ++e)
							t[e] = this.DM & ~this[e];
						return t.t = this.t,
							t.s = ~this.s,
							t
					}
					,
					e.prototype.shiftLeft = function(t) {
						var e = r();
						return t < 0 ? this.rShiftTo(-t, e) : this.lShiftTo(t, e),
							e
					}
					,
					e.prototype.shiftRight = function(t) {
						var e = r();
						return t < 0 ? this.lShiftTo(-t, e) : this.rShiftTo(t, e),
							e
					}
					,
					e.prototype.getLowestSetBit = function() {
						for (var t = 0; t < this.t; ++t)
							if (0 != this[t])
								return t * this.DB + function(t) {
									if (0 == t)
										return -1;
									var e = 0;
									return 0 == (65535 & t) && (t >>= 16,
										e += 16),
										0 == (255 & t) && (t >>= 8,
											e += 8),
										0 == (15 & t) && (t >>= 4,
											e += 4),
										0 == (3 & t) && (t >>= 2,
											e += 2),
										0 == (1 & t) && ++e,
										e
								}(this[t]);
						return this.s < 0 ? this.t * this.DB : -1
					}
					,
					e.prototype.bitCount = function() {
						for (var t = 0, e = this.s & this.DM, r = 0; r < this.t; ++r)
							t += function(t) {
								for (var e = 0; 0 != t;)
									t &= t - 1,
										++e;
								return e
							}(this[r] ^ e);
						return t
					}
					,
					e.prototype.testBit = function(t) {
						var e = Math.floor(t / this.DB);
						return e >= this.t ? 0 != this.s : 0 != (this[e] & 1 << t % this.DB)
					}
					,
					e.prototype.setBit = function(t) {
						return this.changeBit(t, y)
					}
					,
					e.prototype.clearBit = function(t) {
						return this.changeBit(t, m)
					}
					,
					e.prototype.flipBit = function(t) {
						return this.changeBit(t, d)
					}
					,
					e.prototype.add = function(t) {
						var e = r();
						return this.addTo(t, e),
							e
					}
					,
					e.prototype.subtract = function(t) {
						var e = r();
						return this.subTo(t, e),
							e
					}
					,
					e.prototype.multiply = function(t) {
						var e = r();
						return this.multiplyTo(t, e),
							e
					}
					,
					e.prototype.divide = function(t) {
						var e = r();
						return this.divRemTo(t, e, null),
							e
					}
					,
					e.prototype.remainder = function(t) {
						var e = r();
						return this.divRemTo(t, null, e),
							e
					}
					,
					e.prototype.divideAndRemainder = function(t) {
						var e = r()
							, i = r();
						return this.divRemTo(t, e, i),
							new Array(e, i)
					}
					,
					e.prototype.modPow = function(t, e) {
						var i = t.bitLength()
							, n = a(1);
						if (i <= 0)
							return n;
						var o = i < 18 ? 1 : i < 48 ? 3 : i < 144 ? 4 : i < 768 ? 5 : 6
							, s = new (i < 8 ? f : e.isEven() ? b : p)(e)
							, h = new Array
							, u = 3
							, l = o - 1
							, y = (1 << o) - 1;
						if (h[1] = s.convert(this),
							1 < o) {
							var d = r();
							for (s.sqrTo(h[1], d); u <= y;)
								h[u] = r(),
									s.mulTo(d, h[u - 2], h[u]),
									u += 2
						}
						var m, v, g = t.t - 1, T = !0, w = r();
						for (i = c(t[g]) - 1; 0 <= g;) {
							for (l <= i ? m = t[g] >> i - l & y : (m = (t[g] & (1 << i + 1) - 1) << l - i,
								0 < g && (m |= t[g - 1] >> this.DB + i - l)),
								u = o; 0 == (1 & m);)
								m >>= 1,
									--u;
							if ((i -= u) < 0 && (i += this.DB,
								--g),
								T)
								h[m].copyTo(n),
									T = !1;
							else {
								for (; 1 < u;)
									s.sqrTo(n, w),
										s.sqrTo(w, n),
										u -= 2;
								0 < u ? s.sqrTo(n, w) : (v = n,
									n = w,
									w = v),
									s.mulTo(w, h[m], n)
							}
							for (; 0 <= g && 0 == (t[g] & 1 << i);)
								s.sqrTo(n, w),
									v = n,
									n = w,
									w = v,
									--i < 0 && (i = this.DB - 1,
										--g)
						}
						return s.revert(n)
					}
					,
					e.prototype.modInverse = function(t) {
						var r = t.isEven();
						if (this.isEven() && r || 0 == t.signum())
							return e.ZERO;
						for (var i = t.clone(), n = this.clone(), o = a(1), s = a(0), h = a(0), u = a(1); 0 != i.signum();) {
							for (; i.isEven();)
								i.rShiftTo(1, i),
									r ? (o.isEven() && s.isEven() || (o.addTo(this, o),
										s.subTo(t, s)),
										o.rShiftTo(1, o)) : s.isEven() || s.subTo(t, s),
									s.rShiftTo(1, s);
							for (; n.isEven();)
								n.rShiftTo(1, n),
									r ? (h.isEven() && u.isEven() || (h.addTo(this, h),
										u.subTo(t, u)),
										h.rShiftTo(1, h)) : u.isEven() || u.subTo(t, u),
									u.rShiftTo(1, u);
							0 <= i.compareTo(n) ? (i.subTo(n, i),
								r && o.subTo(h, o),
								s.subTo(u, s)) : (n.subTo(i, n),
									r && h.subTo(o, h),
									u.subTo(s, u))
						}
						return 0 != n.compareTo(e.ONE) ? e.ZERO : 0 <= u.compareTo(t) ? u.subtract(t) : u.signum() < 0 ? (u.addTo(t, u),
							u.signum() < 0 ? u.add(t) : u) : u
					}
					,
					e.prototype.pow = function(t) {
						return this.exp(t, new v)
					}
					,
					e.prototype.gcd = function(t) {
						var e = this.s < 0 ? this.negate() : this.clone()
							, r = t.s < 0 ? t.negate() : t.clone();
						e.compareTo(r) < 0 && (n = e,
							e = r,
							r = n);
						var i = e.getLowestSetBit()
							, n = r.getLowestSetBit();
						if (n < 0)
							return e;
						for (0 < (n = i < n ? i : n) && (e.rShiftTo(n, e),
							r.rShiftTo(n, r)); 0 < e.signum();)
							0 < (i = e.getLowestSetBit()) && e.rShiftTo(i, e),
								0 < (i = r.getLowestSetBit()) && r.rShiftTo(i, r),
								0 <= e.compareTo(r) ? (e.subTo(r, e),
									e.rShiftTo(1, e)) : (r.subTo(e, r),
										r.rShiftTo(1, r));
						return 0 < n && r.lShiftTo(n, r),
							r
					}
					,
					e.prototype.isProbablePrime = function(t) {
						var e, r = this.abs();
						if (1 == r.t && r[0] <= w[w.length - 1]) {
							for (e = 0; e < w.length; ++e)
								if (r[0] == w[e])
									return !0;
							return !1
						}
						if (r.isEven())
							return !1;
						for (e = 1; e < w.length;) {
							for (var i = w[e], n = e + 1; n < w.length && i < F;)
								i *= w[n++];
							for (i = r.modInt(i); e < n;)
								if (i % w[e++] == 0)
									return !1
						}
						return r.millerRabin(t)
					}
					,
					e.prototype.square = function() {
						var t = r();
						return this.squareTo(t),
							t
					}
					,
					e.prototype.Barrett = b;
				var x = new Array
					, B = 0;
				if ("undefined" != typeof window && window.crypto)
					if (window.crypto.getRandomValues) {
						var D = new Uint8Array(32);
						for (window.crypto.getRandomValues(D),
							A = 0; A < 32; ++A)
							x[B++] = D[A]
					} else if ("Netscape" == navigator.appName && navigator.appVersion < "5")
						for (var E = window.crypto.random(32), A = 0; A < E.length; ++A)
							x[B++] = 255 & E.charCodeAt(A);
				for (; B < O;)
					A = Math.floor(65536 * Math.random()),
						x[B++] = A >>> 8,
						x[B++] = 255 & A;
				function I() {
					if (null == T) {
						for (S(),
							(T = new R).init(x),
							B = 0; B < x.length; ++B)
							x[B] = 0;
						B = 0
					}
					return T.next()
				}
				function q() { }
				function R() {
					this.i = 0,
						this.j = 0,
						this.S = new Array
				}
				B = 0,
					S(),
					q.prototype.nextBytes = function(t) {
						for (var e = 0; e < t.length; ++e)
							t[e] = I()
					}
					,
					R.prototype.init = function(t) {
						for (var e, r, i = 0; i < 256; ++i)
							this.S[i] = i;
						for (i = e = 0; i < 256; ++i)
							e = e + this.S[i] + t[i % t.length] & 255,
								r = this.S[i],
								this.S[i] = this.S[e],
								this.S[e] = r;
						this.i = 0,
							this.j = 0
					}
					,
					R.prototype.next = function() {
						var t;
						return this.i = this.i + 1 & 255,
							this.j = this.j + this.S[this.i] & 255,
							t = this.S[this.i],
							this.S[this.i] = this.S[this.j],
							this.S[this.j] = t,
							this.S[t + this.S[this.i] & 255]
					}
					;
				var O = 256;
				t.exports = {
					default: e,
					BigInteger: e,
					SecureRandom: q
				}
			}
			).call(this)
		},
		686: function(t, e, r) {
			function i(t) {
				if (o[t])
					return o[t].exports;
				var e = o[t] = {
					i: t,
					l: !1,
					exports: {}
				};
				return n[t].call(e.exports, e, e.exports, i),
					e.l = !0,
					e.exports
			}
			var n, o;
			t.exports = (o = {},
				i.m = n = [function(t, e) {
					t.exports = r(77)
				}
					, function(t, e, r) {
						"use strict";
						function i(t, e) {
							for (var r = [], i = ~~(e / 8), n = e % 8, o = 0, s = t.length; o < s; o++)
								r[o] = (t[(o + i) % s] << n & 255) + (t[(o + i + 1) % s] >>> 8 - n & 255);
							return r
						}
						function n(t, e) {
							for (var r = [], i = t.length - 1; 0 <= i; i--)
								r[i] = 255 & (t[i] ^ e[i]);
							return r
						}
						function o(t, e) {
							for (var r = [], i = t.length - 1; 0 <= i; i--)
								r[i] = t[i] & e[i] & 255;
							return r
						}
						function s(t, e) {
							for (var r = [], i = t.length - 1; 0 <= i; i--)
								r[i] = 255 & (t[i] | e[i]);
							return r
						}
						function h(t, e) {
							for (var r = [], i = 0, n = t.length - 1; 0 <= n; n--) {
								var o = t[n] + e[n] + i;
								i = 255 < o ? 1 : 0,
									r[n] = 255 & o
							}
							return r
						}
						function u(t, e, r, i) {
							return 0 <= i && i <= 15 ? n(n(t, e), r) : s(o(t, e), o(function(t) {
								for (var e = [], r = t.length - 1; 0 <= r; r--)
									e[r] = 255 & ~t[r];
								return e
							}(t), r))
						}
						function a(t, e) {
							for (var r = [], a = [], c = 0; c < 16; c++) {
								var f = 4 * c;
								r.push(e.slice(f, 4 + f))
							}
							for (var p, l = 16; l < 68; l++)
								r.push(n(n((p = n(n(r[l - 16], r[l - 9]), i(r[l - 3], 15)),
									n(n(p, i(p, 15)), i(p, 23))), i(r[l - 13], 7)), r[l - 6]));
							for (var y = 0; y < 64; y++)
								a.push(n(r[y], r[y + 4]));
							for (var d, m, v = [121, 204, 69, 25], g = [122, 135, 157, 138], b = t.slice(0, 4), T = t.slice(4, 8), w = t.slice(8, 12), F = t.slice(12, 16), S = t.slice(16, 20), x = t.slice(20, 24), B = t.slice(24, 28), D = t.slice(28, 32), E = void 0, A = 0; A < 64; A++) {
								var I = 0 <= A && A <= 15 ? v : g
									, q = n(E = i(h(h(i(b, 12), S), i(I, A)), 7), i(b, 12))
									, R = h(h(h((d = b,
										m = T,
										R = w,
										0 <= (I = A) && I <= 15 ? n(n(d, m), R) : s(s(o(d, m), o(d, R)), o(m, R))), F), q), a[A]);
								q = h(h(h(u(S, x, B, A), D), E), r[A]),
									F = w,
									w = i(T, 9),
									T = b,
									b = R,
									D = B,
									B = i(x, 19),
									x = S,
									S = n(n(q = q, i(q, 9)), i(q, 17))
							}
							return n([].concat(b, T, w, F, S, x, B, D), t)
						}
						t.exports = function(t) {
							for (var e = 448 <= (e = (h = 8 * t.length) % 512) ? 512 - e % 448 - 1 : 448 - e - 1, r = new Array((e - 7) / 8), i = 0, n = r.length; i < n; i++)
								r[i] = 0;
							for (var o, s = [], h = h.toString(2), u = 7; 0 <= u; u--)
								8 < h.length ? (o = h.length - 8,
									s[u] = parseInt(h.substr(o), 2),
									h = h.substr(0, o)) : 0 < h.length ? (s[u] = parseInt(h, 2),
										h = "") : s[u] = 0;
							for (var c = [].concat(t, [128], r, s), f = c.length / 64, p = [115, 128, 22, 111, 73, 20, 178, 185, 23, 36, 66, 215, 218, 138, 6, 0, 169, 111, 48, 188, 22, 49, 56, 170, 227, 141, 238, 77, 176, 251, 14, 78], l = 0; l < f; l++) {
								var y = 64 * l;
								p = a(p, c.slice(y, 64 + y))
							}
							return p
						}
					}
					, function(t, e, r) {
						"use strict";
						t.exports = {
							sm2: r(3),
							sm3: r(7),
							sm4: r(8)
						}
					}
					, function(t, e, r) {
						"use strict";
						var i = r(0).BigInteger
							, n = r(4)
							, o = n.encodeDer
							, s = n.decodeDer
							, h = r(5)
							, u = r(1)
							, a = (r = h.generateEcparam()).G
							, c = r.curve
							, f = r.n;
						function p(t, e, r) {
							var i = h.utf8ToHex(i = 2 < arguments.length && void 0 !== r ? r : "1234567812345678")
								, n = h.leftPad(a.curve.a.toBigInteger().toRadix(16), 64)
								, o = h.leftPad(a.curve.b.toBigInteger().toRadix(16), 64)
								, s = h.leftPad(a.getX().toBigInteger().toRadix(16), 64)
								, c = h.leftPad(a.getY().toBigInteger().toRadix(16), 64);
							return r = (e = 128 < e.length ? e.substr(2, 128) : e).substr(0, 64),
								e = e.substr(64, 64),
								e = h.hexToArray(i + n + o + s + c + r + e),
								i = 4 * i.length,
								e.unshift(255 & i),
								e.unshift(i >> 8 & 255),
								e = u(e),
								h.arrayToHex(u(e.concat(h.hexToArray(t))))
						}
						function l() {
							var t = h.generateKeyPairHex()
								, e = c.decodePointHex(t.publicKey);
							return t.k = new i(t.privateKey, 16),
								t.x1 = e.getX().toBigInteger(),
								t
						}
						t.exports = {
							generateKeyPairHex: h.generateKeyPairHex,
							doEncrypt: function(t, e) {
								var r = 2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : 1;
								t = h.hexToArray(h.utf8ToHex(t)),
									e = h.getGlobalCurve().decodePointHex(e);
								var n = h.generateKeyPairHex()
									, o = new i(n.privateKey, 16)
									, s = n.publicKey;
								function a() {
									p = u([].concat(l, [c >> 24 & 255, c >> 16 & 255, c >> 8 & 255, 255 & c])),
										c++,
										f = 0
								}
								128 < s.length && (s = s.substr(s.length - 128)),
									n = e.multiply(o),
									e = h.hexToArray(h.leftPad(n.getX().toBigInteger().toRadix(16), 64)),
									o = h.hexToArray(h.leftPad(n.getY().toBigInteger().toRadix(16), 64)),
									n = h.arrayToHex(u([].concat(e, t, o)));
								var c = 1
									, f = 0
									, p = []
									, l = [].concat(e, o);
								a();
								for (var y = 0, d = t.length; y < d; y++)
									f === p.length && a(),
										t[y] ^= 255 & p[f++];
								return o = h.arrayToHex(t),
									0 === r ? s + o + n : s + n + o
							},
							doDecrypt: function(t, e) {
								var r = 2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : 1;
								e = new i(e, 16);
								var n = t.substr(128, 64)
									, o = t.substr(192);
								function s() {
									p = u([].concat(l, [c >> 24 & 255, c >> 16 & 255, c >> 8 & 255, 255 & c])),
										c++,
										f = 0
								}
								0 === r && (n = t.substr(t.length - 64),
									o = t.substr(128, t.length - 128 - 64));
								var a = h.hexToArray(o)
									, c = (t = h.getGlobalCurve().decodePointHex("04" + t.substr(0, 128)).multiply(e),
										e = h.hexToArray(h.leftPad(t.getX().toBigInteger().toRadix(16), 64)),
										t = h.hexToArray(h.leftPad(t.getY().toBigInteger().toRadix(16), 64)),
										1)
									, f = 0
									, p = []
									, l = [].concat(e, t);
								s();
								for (var y = 0, d = a.length; y < d; y++)
									f === p.length && s(),
										a[y] ^= 255 & p[f++];
								return h.arrayToHex(u([].concat(e, a, t))) === n ? h.arrayToUtf8(a) : ""
							},
							doSignature: function(t, e) {
								var r = (c = 2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : {}).pointPool
									, n = c.der
									, s = c.hash
									, u = c.publicKey
									, c = c.userId;
								t = "string" == typeof t ? h.utf8ToHex(t) : h.arrayToHex(t),
									s && (t = p(t, u || (s = e,
										u = a.multiply(new i(s, 16)),
										"04" + (s = h.leftPad(u.getX().toBigInteger().toString(16), 64)) + (u = h.leftPad(u.getY().toBigInteger().toString(16), 64))), c));
								var y = new i(e, 16)
									, d = new i(t, 16)
									, m = null
									, v = null
									, g = null;
								do {
									do {
										var b = void 0;
										m = (b = r && r.length ? r.pop() : l()).k,
											v = d.add(b.x1).mod(f)
									} while (v.equals(i.ZERO) || v.add(m).equals(f))
								} while ((g = y.add(i.ONE).modInverse(f).multiply(m.subtract(v.multiply(y))).mod(f)).equals(i.ZERO));
								return n ? o(v, g) : h.leftPad(v.toString(16), 64) + h.leftPad(g.toString(16), 64)
							},
							doVerifySignature: function(t, e, r) {
								var n = (u = 3 < arguments.length && void 0 !== arguments[3] ? arguments[3] : {}).der
									, o = u.hash
									, u = u.userId;
								return t = "string" == typeof t ? h.utf8ToHex(t) : h.arrayToHex(t),
									o && (t = p(t, r, u)),
									o = void 0,
									u = void 0,
									u = n ? (o = (n = s(e)).r,
										n.s) : (o = new i(e.substring(0, 64), 16),
											new i(e.substring(64), 16)),
									e = c.decodePointHex(r),
									r = new i(t, 16),
									!(t = o.add(u).mod(f)).equals(i.ZERO) && (t = a.multiply(u).add(e.multiply(t)),
										t = r.add(t.getX().toBigInteger()).mod(f),
										o.equals(t))
							},
							getPoint: l,
							verifyPublicKey: h.verifyPublicKey
						}
					}
					, function(t, e, r) {
						"use strict";
						function i(t, e) {
							if (!t)
								throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
							return !e || "object" != typeof e && "function" != typeof e ? t : e
						}
						function n(t, e) {
							if ("function" != typeof e && null !== e)
								throw new TypeError("Super expression must either be null or a function, not " + typeof e);
							t.prototype = Object.create(e && e.prototype, {
								constructor: {
									value: t,
									enumerable: !1,
									writable: !0,
									configurable: !0
								}
							}),
								e && (Object.setPrototypeOf ? Object.setPrototypeOf(t, e) : t.__proto__ = e)
						}
						function o(t, e) {
							if (!(t instanceof e))
								throw new TypeError("Cannot call a class as a function")
						}
						var s = r(0).BigInteger;
						function h() {
							o(this, h),
								this.tlv = null,
								this.t = "00",
								this.l = "00",
								this.v = ""
						}
						h.prototype.getEncodedHex = function() {
							return this.tlv || (this.v = this.getValue(),
								this.l = this.getLength(),
								this.tlv = this.t + this.l + this.v),
								this.tlv
						}
							,
							h.prototype.getLength = function() {
								var t = this.v.length / 2
									, e = t.toString(16);
								return e.length % 2 == 1 && (e = "0" + e),
									t < 128 ? e : (128 + e.length / 2).toString(16) + e
							}
							,
							h.prototype.getValue = function() {
								return ""
							}
							;
						var u, a = (n(c, u = r = h),
							c.prototype.getValue = function() {
								return this.v
							}
							,
							c);
						function c(t) {
							o(this, c);
							var e = i(this, u.call(this));
							return e.t = "02",
								t && (e.v = function(t) {
									if ("-" !== (e = t.toString(16))[0])
										e.length % 2 == 1 ? e = "0" + e : e.match(/^[0-7]/) || (e = "00" + e);
									else {
										var e, r = (e = e.substr(1)).length;
										r % 2 == 1 ? r += 1 : e.match(/^[0-7]/) || (r += 2);
										for (var i = "", n = 0; n < r; n++)
											i += "f";
										e = (e = (i = new s(i, 16)).xor(t).add(s.ONE)).toString(16).replace(/^-/, "")
									}
									return e
								}(t)),
								e
						}
						var f, p = (n(l, f = r),
							l.prototype.getValue = function() {
								return this.v = this.asn1Array.map((function(t) {
									return t.getEncodedHex()
								}
								)).join(""),
									this.v
							}
							,
							l);
						function l(t) {
							o(this, l);
							var e = i(this, f.call(this));
							return e.t = "30",
								e.asn1Array = t,
								e
						}
						function y(t, e) {
							return +t[e + 2] < 8 ? 1 : 128 & +t.substr(e + 2, 2)
						}
						function d(t, e) {
							var r = y(t, e);
							return (r = t.substr(e + 2, 2 * r)) ? (+r[0] < 8 ? new s(r, 16) : new s(r.substr(2), 16)).intValue() : -1
						}
						function m(t, e) {
							return e + 2 * (y(t, e) + 1)
						}
						t.exports = {
							encodeDer: function(t, e) {
								return t = new a(t),
									e = new a(e),
									new p([t, e]).getEncodedHex()
							},
							decodeDer: function(t) {
								var e = m(t, 0)
									, r = m(t, e)
									, i = d(t, e);
								return e = t.substr(r, 2 * i),
									r = m(t, i = r + e.length),
									i = d(t, i),
									i = t.substr(r, 2 * i),
								{
									r: new s(e, 16),
									s: new s(i, 16)
								}
							}
						}
					}
					, function(t, e, r) {
						"use strict";
						var i = (n = r(0)).BigInteger
							, n = n.SecureRandom
							, o = r(6).ECCurveFp
							, s = new n
							, h = (n = c()).curve
							, u = n.G
							, a = n.n;
						function c() {
							var t = new i("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF", 16)
								, e = new i("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC", 16)
								, r = new i("28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93", 16);
							return r = (e = new o(t, e, r)).decodePointHex("0432C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7BC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0"),
							{
								curve: e,
								G: r,
								n: new i("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123", 16)
							}
						}
						function f(t, e) {
							return t.length >= e ? t : new Array(e - t.length + 1).join("0") + t
						}
						t.exports = {
							getGlobalCurve: function() {
								return h
							},
							generateEcparam: c,
							generateKeyPairHex: function(t, e, r) {
								return {
									privateKey: r = f((e = (t ? new i(t, e, r) : new i(a.bitLength(), s)).mod(a.subtract(i.ONE)).add(i.ONE)).toString(16), 64),
									publicKey: "04" + f((e = u.multiply(e)).getX().toBigInteger().toString(16), 64) + f(e.getY().toBigInteger().toString(16), 64)
								}
							},
							utf8ToHex: function(t) {
								for (var e = (t = unescape(encodeURIComponent(t))).length, r = [], i = 0; i < e; i++)
									r[i >>> 2] |= (255 & t.charCodeAt(i)) << 24 - i % 4 * 8;
								for (var n = [], o = 0; o < e; o++) {
									var s = r[o >>> 2] >>> 24 - o % 4 * 8 & 255;
									n.push((s >>> 4).toString(16)),
										n.push((15 & s).toString(16))
								}
								return n.join("")
							},
							leftPad: f,
							arrayToHex: function(t) {
								return t.map((function(t) {
									return 1 === (t = t.toString(16)).length ? "0" + t : t
								}
								)).join("")
							},
							arrayToUtf8: function(t) {
								for (var e = [], r = 0, i = 0; i < 2 * t.length; i += 2)
									e[i >>> 3] |= parseInt(t[r], 10) << 24 - i % 8 * 4,
										r++;
								try {
									for (var n = [], o = 0; o < t.length; o++) {
										var s = e[o >>> 2] >>> 24 - o % 4 * 8 & 255;
										n.push(String.fromCharCode(s))
									}
									return decodeURIComponent(escape(n.join("")))
								} catch (t) {
									throw new Error("Malformed UTF-8 data")
								}
							},
							hexToArray: function(t) {
								for (var e = [], r = (t = (r = t.length) % 2 != 0 ? f(t, r + 1) : t).length, i = 0; i < r; i += 2)
									e.push(parseInt(t.substr(i, 2), 16));
								return e
							},
							verifyPublicKey: function(t) {
								var e = h.decodePointHex(t);
								return !!e && (t = e.getX(),
									e.getY().square().equals(t.multiply(t.square()).add(t.multiply(h.a)).add(h.b)))
							}
						}
					}
					, function(t, e, r) {
						"use strict";
						function i(t, e) {
							if (!(t instanceof e))
								throw new TypeError("Cannot call a class as a function")
						}
						var n = r(0).BigInteger
							, o = new n("3")
							, s = (h.prototype.equals = function(t) {
								return t === this || this.q.equals(t.q) && this.x.equals(t.x)
							}
								,
								h.prototype.toBigInteger = function() {
									return this.x
								}
								,
								h.prototype.negate = function() {
									return new h(this.q, this.x.negate().mod(this.q))
								}
								,
								h.prototype.add = function(t) {
									return new h(this.q, this.x.add(t.toBigInteger()).mod(this.q))
								}
								,
								h.prototype.subtract = function(t) {
									return new h(this.q, this.x.subtract(t.toBigInteger()).mod(this.q))
								}
								,
								h.prototype.multiply = function(t) {
									return new h(this.q, this.x.multiply(t.toBigInteger()).mod(this.q))
								}
								,
								h.prototype.divide = function(t) {
									return new h(this.q, this.x.multiply(t.toBigInteger().modInverse(this.q)).mod(this.q))
								}
								,
								h.prototype.square = function() {
									return new h(this.q, this.x.square().mod(this.q))
								}
								,
								h);
						function h(t, e) {
							i(this, h),
								this.x = e,
								this.q = t
						}
						var u = (a.prototype.getX = function() {
							return null === this.zinv && (this.zinv = this.z.modInverse(this.curve.q)),
								this.curve.fromBigInteger(this.x.toBigInteger().multiply(this.zinv).mod(this.curve.q))
						}
							,
							a.prototype.getY = function() {
								return null === this.zinv && (this.zinv = this.z.modInverse(this.curve.q)),
									this.curve.fromBigInteger(this.y.toBigInteger().multiply(this.zinv).mod(this.curve.q))
							}
							,
							a.prototype.equals = function(t) {
								return t === this || (this.isInfinity() ? t.isInfinity() : t.isInfinity() ? this.isInfinity() : !!t.y.toBigInteger().multiply(this.z).subtract(this.y.toBigInteger().multiply(t.z)).mod(this.curve.q).equals(n.ZERO) && t.x.toBigInteger().multiply(this.z).subtract(this.x.toBigInteger().multiply(t.z)).mod(this.curve.q).equals(n.ZERO))
							}
							,
							a.prototype.isInfinity = function() {
								return null === this.x && null === this.y || this.z.equals(n.ZERO) && !this.y.toBigInteger().equals(n.ZERO)
							}
							,
							a.prototype.negate = function() {
								return new a(this.curve, this.x, this.y.negate(), this.z)
							}
							,
							a.prototype.add = function(t) {
								if (this.isInfinity())
									return t;
								if (t.isInfinity())
									return this;
								var e = this.x.toBigInteger()
									, r = this.y.toBigInteger()
									, i = this.z
									, o = t.x.toBigInteger()
									, s = t.y.toBigInteger()
									, h = t.z
									, u = this.curve.q
									, c = e.multiply(h).mod(u);
								return t = o.multiply(i).mod(u),
									e = c.subtract(t),
									o = r.multiply(h).mod(u),
									r = s.multiply(i).mod(u),
									s = o.subtract(r),
									n.ZERO.equals(e) ? n.ZERO.equals(s) ? this.twice() : this.curve.infinity : (r = c.add(t),
										t = i.multiply(h).mod(u),
										i = e.square().mod(u),
										h = e.multiply(i).mod(u),
										r = t.multiply(s.square()).subtract(r.multiply(i)).mod(u),
										e = e.multiply(r).mod(u),
										o = s.multiply(i.multiply(c).subtract(r)).subtract(o.multiply(h)).mod(u),
										u = h.multiply(t).mod(u),
										new a(this.curve, this.curve.fromBigInteger(e), this.curve.fromBigInteger(o), u))
							}
							,
							a.prototype.twice = function() {
								if (this.isInfinity())
									return this;
								if (!this.y.toBigInteger().signum())
									return this.curve.infinity;
								var t = this.x.toBigInteger()
									, e = this.y.toBigInteger()
									, r = this.z
									, i = this.curve.q
									, n = this.curve.a.toBigInteger()
									, s = t.square().multiply(o).add(n.multiply(r.square())).mod(i)
									, h = e.shiftLeft(1).multiply(r).mod(i)
									, u = (n = (u = e.square().mod(i)).multiply(t).multiply(r).mod(i),
										e = h.square().mod(i),
										t = s.square().subtract(n.shiftLeft(3)).mod(i),
										r = h.multiply(t).mod(i),
										s.multiply(n.shiftLeft(2).subtract(t)).subtract(e.shiftLeft(1).multiply(u)).mod(i));
								return i = h.multiply(e).mod(i),
									new a(this.curve, this.curve.fromBigInteger(r), this.curve.fromBigInteger(u), i)
							}
							,
							a.prototype.multiply = function(t) {
								if (this.isInfinity())
									return this;
								if (!t.signum())
									return this.curve.infinity;
								for (var e = t.multiply(o), r = this.negate(), i = this, n = e.bitLength() - 2; 0 < n; n--) {
									i = i.twice();
									var s = e.testBit(n);
									s !== t.testBit(n) && (i = i.add(s ? this : r))
								}
								return i
							}
							,
							a);
						function a(t, e, r, o) {
							i(this, a),
								this.curve = t,
								this.x = e,
								this.y = r,
								this.z = null == o ? n.ONE : o,
								this.zinv = null
						}
						function c(t, e, r) {
							i(this, c),
								this.q = t,
								this.a = this.fromBigInteger(e),
								this.b = this.fromBigInteger(r),
								this.infinity = new u(this, null, null)
						}
						c.prototype.equals = function(t) {
							return t === this || this.q.equals(t.q) && this.a.equals(t.a) && this.b.equals(t.b)
						}
							,
							c.prototype.fromBigInteger = function(t) {
								return new s(this.q, t)
							}
							,
							c.prototype.decodePointHex = function(t) {
								switch (parseInt(t.substr(0, 2), 16)) {
									case 0:
										return this.infinity;
									default:
										return null;
									case 4:
									case 6:
									case 7:
										var e = (t.length - 2) / 2
											, r = t.substr(2, e);
										return e = t.substr(2 + e, e),
											new u(this, this.fromBigInteger(new n(r, 16)), this.fromBigInteger(new n(e, 16)))
								}
							}
							,
							r = c,
							t.exports = {
								ECPointFp: u,
								ECCurveFp: r
							}
					}
					, function(t, e, r) {
						"use strict";
						var i = r(1);
						t.exports = function(t) {
							return t = "string" == typeof t ? function(t) {
								for (var e = [], r = 0, i = t.length; r < i; r++) {
									var n = t.charCodeAt(r);
									if (n <= 127)
										e.push(n);
									else if (n <= 2047)
										e.push(192 | n >>> 6),
											e.push(128 | 63 & n);
									else if (n <= 55295 || 57344 <= n && n <= 65535)
										e.push(224 | n >>> 12),
											e.push(128 | n >>> 6 & 63),
											e.push(128 | 63 & n);
									else {
										if (!(65536 <= n && n <= 1114111))
											throw e.push(n),
											new Error("input is not supported");
										r++,
											e.push(240 | n >>> 18 & 28),
											e.push(128 | n >>> 12 & 63),
											e.push(128 | n >>> 6 & 63),
											e.push(128 | 63 & n)
									}
								}
								return e
							}(t) : Array.prototype.slice.call(t),
								i(t).map((function(t) {
									return 1 === (t = t.toString(16)).length ? "0" + t : t
								}
								)).join("")
						}
					}
					, function(t, e, r) {
						"use strict";
						var i = [214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 170, 68, 19, 38, 73, 134, 6, 153, 156, 66, 80, 244, 145, 239, 152, 122, 51, 84, 11, 67, 237, 207, 172, 98, 228, 179, 28, 169, 201, 8, 232, 149, 128, 223, 148, 250, 117, 143, 63, 166, 71, 7, 167, 252, 243, 115, 23, 186, 131, 89, 60, 25, 230, 133, 79, 168, 104, 107, 129, 178, 113, 100, 218, 139, 248, 235, 15, 75, 112, 86, 157, 53, 30, 36, 14, 94, 99, 88, 209, 162, 37, 34, 124, 59, 1, 33, 120, 135, 212, 0, 70, 87, 159, 211, 39, 82, 76, 54, 2, 231, 160, 196, 200, 158, 234, 191, 138, 210, 64, 199, 56, 181, 163, 247, 242, 206, 249, 97, 21, 161, 224, 174, 93, 164, 155, 52, 26, 85, 173, 147, 50, 48, 245, 140, 177, 227, 29, 246, 226, 46, 130, 102, 202, 96, 192, 41, 35, 171, 13, 83, 78, 111, 213, 219, 55, 69, 222, 253, 142, 47, 3, 255, 106, 114, 109, 108, 91, 81, 141, 27, 175, 146, 187, 221, 188, 127, 17, 217, 92, 65, 31, 16, 90, 216, 10, 193, 49, 136, 165, 205, 123, 189, 45, 116, 208, 18, 184, 229, 180, 176, 137, 105, 151, 74, 12, 150, 119, 126, 101, 185, 241, 9, 197, 110, 198, 132, 24, 240, 125, 236, 58, 220, 77, 32, 121, 238, 95, 62, 215, 203, 57, 72]
							, n = [462357, 472066609, 943670861, 1415275113, 1886879365, 2358483617, 2830087869, 3301692121, 3773296373, 4228057617, 404694573, 876298825, 1347903077, 1819507329, 2291111581, 2762715833, 3234320085, 3705924337, 4177462797, 337322537, 808926789, 1280531041, 1752135293, 2223739545, 2695343797, 3166948049, 3638552301, 4110090761, 269950501, 741554753, 1213159005, 1684763257];
						function o(t) {
							for (var e = [], r = 0, i = t.length; r < i; r += 2)
								e.push(parseInt(t.substr(r, 2), 16));
							return e
						}
						function s(t, e) {
							return t << e | t >>> 32 - e
						}
						function h(t) {
							return (255 & i[t >>> 24 & 255]) << 24 | (255 & i[t >>> 16 & 255]) << 16 | (255 & i[t >>> 8 & 255]) << 8 | 255 & i[255 & t]
						}
						function u(t) {
							return t ^ s(t, 2) ^ s(t, 10) ^ s(t, 18) ^ s(t, 24)
						}
						function a(t) {
							return t ^ s(t, 13) ^ s(t, 23)
						}
						function c(t, e, r, i) {
							i = void 0 === (c = (f = 3 < arguments.length && void 0 !== i ? i : {}).padding) ? "pkcs#5" : c;
							var s = f.mode
								, c = void 0 === (c = f.iv) ? [] : c
								, f = void 0 === (f = f.output) ? "string" : f;
							if ("cbc" === s && 16 !== (c = "string" == typeof c ? o(c) : c).length)
								throw new Error("iv is invalid");
							if (16 !== (e = "string" == typeof e ? o(e) : e).length)
								throw new Error("key is invalid");
							if (t = "string" == typeof t ? (0 !== r ? function(t) {
								for (var e = [], r = 0, i = t.length; r < i; r++) {
									var n = t.charCodeAt(r);
									if (n <= 127)
										e.push(n);
									else if (n <= 2047)
										e.push(192 | n >>> 6),
											e.push(128 | 63 & n);
									else if (n <= 55295 || 57344 <= n && n <= 65535)
										e.push(224 | n >>> 12),
											e.push(128 | n >>> 6 & 63),
											e.push(128 | 63 & n);
									else {
										if (!(65536 <= n && n <= 1114111))
											throw e.push(n),
											new Error("input is not supported");
										r++,
											e.push(240 | n >>> 18 & 28),
											e.push(128 | n >>> 12 & 63),
											e.push(128 | n >>> 6 & 63),
											e.push(128 | 63 & n)
									}
								}
								return e
							}
								: o)(t) : [].concat(t),
								"pkcs#5" === i && 0 !== r)
								for (var p = 16 - t.length % 16, l = 0; l < p; l++)
									t.push(p);
							var y = new Array(32);
							!function(t, e, r) {
								for (var i = new Array(4), o = new Array(4), s = 0; s < 4; s++)
									o[0] = 255 & t[0 + 4 * s],
										o[1] = 255 & t[1 + 4 * s],
										o[2] = 255 & t[2 + 4 * s],
										o[3] = 255 & t[3 + 4 * s],
										i[s] = o[0] << 24 | o[1] << 16 | o[2] << 8 | o[3];
								i[0] ^= 2746333894,
									i[1] ^= 1453994832,
									i[2] ^= 1736282519,
									i[3] ^= 2993693404;
								for (var u, c = 0; c < 32; c += 4)
									u = i[1] ^ i[2] ^ i[3] ^ n[c + 0],
										e[c + 0] = i[0] ^= a(h(u)),
										u = i[2] ^ i[3] ^ i[0] ^ n[c + 1],
										e[c + 1] = i[1] ^= a(h(u)),
										u = i[3] ^ i[0] ^ i[1] ^ n[c + 2],
										e[c + 2] = i[2] ^= a(h(u)),
										u = i[0] ^ i[1] ^ i[2] ^ n[c + 3],
										e[c + 3] = i[3] ^= a(h(u));
								if (0 === r)
									for (var f, p = 0; p < 16; p++)
										f = e[p],
											e[p] = e[31 - p],
											e[31 - p] = f
							}(e, y, r);
							for (var d = [], m = c, v = t.length, g = 0; 16 <= v;) {
								var b = t.slice(g, g + 16)
									, T = new Array(16);
								if ("cbc" === s)
									for (var w = 0; w < 16; w++)
										0 !== r && (b[w] ^= m[w]);
								!function(t, e, r) {
									for (var i = new Array(4), n = new Array(4), o = 0; o < 4; o++)
										n[0] = 255 & t[4 * o],
											n[1] = 255 & t[4 * o + 1],
											n[2] = 255 & t[4 * o + 2],
											n[3] = 255 & t[4 * o + 3],
											i[o] = n[0] << 24 | n[1] << 16 | n[2] << 8 | n[3];
									for (var s, a = 0; a < 32; a += 4)
										s = i[1] ^ i[2] ^ i[3] ^ r[a + 0],
											i[0] ^= u(h(s)),
											s = i[2] ^ i[3] ^ i[0] ^ r[a + 1],
											i[1] ^= u(h(s)),
											s = i[3] ^ i[0] ^ i[1] ^ r[a + 2],
											i[2] ^= u(h(s)),
											s = i[0] ^ i[1] ^ i[2] ^ r[a + 3],
											i[3] ^= u(h(s));
									for (var c = 0; c < 16; c += 4)
										e[c] = i[3 - c / 4] >>> 24 & 255,
											e[c + 1] = i[3 - c / 4] >>> 16 & 255,
											e[c + 2] = i[3 - c / 4] >>> 8 & 255,
											e[c + 3] = 255 & i[3 - c / 4]
								}(b, T, y);
								for (var F = 0; F < 16; F++)
									"cbc" === s && 0 === r && (T[F] ^= m[F]),
										d[g + F] = T[F];
								"cbc" === s && (m = 0 !== r ? T : b),
									v -= 16,
									g += 16
							}
							return "pkcs#5" === i && 0 === r && (i = d[d.length - 1],
								d.splice(d.length - i, i)),
								"array" !== f ? 0 !== r ? d.map((function(t) {
									return 1 === (t = t.toString(16)).length ? "0" + t : t
								}
								)).join("") : function(t) {
									for (var e = [], r = 0, i = t.length; r < i; r++)
										240 <= t[r] && t[r] <= 247 ? (e.push(String.fromCharCode(((7 & t[r]) << 18) + ((63 & t[r + 1]) << 12) + ((63 & t[r + 2]) << 6) + (63 & t[r + 3]))),
											r += 3) : 224 <= t[r] && t[r] <= 239 ? (e.push(String.fromCharCode(((15 & t[r]) << 12) + ((63 & t[r + 1]) << 6) + (63 & t[r + 2]))),
												r += 2) : 192 <= t[r] && t[r] <= 223 ? (e.push(String.fromCharCode(((31 & t[r]) << 6) + (63 & t[r + 1]))),
													r++) : e.push(String.fromCharCode(t[r]));
									return e.join("")
								}(d) : d
						}
						t.exports = {
							encrypt: function(t, e, r) {
								return c(t, e, 1, r)
							},
							decrypt: function(t, e, r) {
								return c(t, e, 0, r)
							}
						}
					}
				],
				i.c = o,
				i.d = function(t, e, r) {
					i.o(t, e) || Object.defineProperty(t, e, {
						enumerable: !0,
						get: r
					})
				}
				,
				i.r = function(t) {
					"undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
						value: "Module"
					}),
						Object.defineProperty(t, "__esModule", {
							value: !0
						})
				}
				,
				i.t = function(t, e) {
					if (1 & e && (t = i(t)),
						8 & e)
						return t;
					if (4 & e && "object" == typeof t && t && t.__esModule)
						return t;
					var r = Object.create(null);
					if (i.r(r),
						Object.defineProperty(r, "default", {
							enumerable: !0,
							value: t
						}),
						2 & e && "string" != typeof t)
						for (var n in t)
							i.d(r, n, function(e) {
								return t[e]
							}
								.bind(null, n));
					return r
				}
				,
				i.n = function(t) {
					var e = t && t.__esModule ? function() {
						return t.default
					}
						: function() {
							return t
						}
						;
					return i.d(e, "a", e),
						e
				}
				,
				i.o = function(t, e) {
					return Object.prototype.hasOwnProperty.call(t, e)
				}
				,
				i.p = "",
				i(i.s = 2))
		}
	}
		, e = {};
	function r(i) {
		var n = e[i];
		return void 0 !== n || (n = e[i] = {
			exports: {}
		},
			t[i].call(n.exports, n, n.exports, r)),
			n.exports
	}
	r.d = function(t, e) {
		for (var i in e)
			r.o(e, i) && !r.o(t, i) && Object.defineProperty(t, i, {
				enumerable: !0,
				get: e[i]
			})
	}
		,
		r.o = function(t, e) {
			return Object.prototype.hasOwnProperty.call(t, e)
		}
		,
		r.r = function(t) {
			"undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
				value: "Module"
			}),
				Object.defineProperty(t, "__esModule", {
					value: !0
				})
		}
		;
	var i = {};
	return function() {
		"use strict";
		function t(t) {
			this.PromiseState = "pending",
				this.PromiseResult = null,
				this.callbacks = [];
			var e = this;
			function r(t) {
				"pending" === e.PromiseState && (e.PromiseResult = t,
					e.PromiseState = "rejected",
					e.callbacks.forEach((function(e) {
						e.onReject(t)
					}
					)))
			}
			try {
				t((function(t) {
					"pending" == e.PromiseState && (e.PromiseState = "fulfilled",
						e.PromiseResult = t,
						e.callbacks.forEach((function(e) {
							e.onResolve(t)
						}
						)))
				}
				), r)
			} catch (t) {
				r(t)
			}
		}
		r.r(i),
			r.d(i, {
				SummerCryptico: function() {
					return c
				},
				default: function() {
					return f
				}
			});
		var e = r(686);
		function n(t, e) {
			var r, i = Object.keys(t);
			return Object.getOwnPropertySymbols && (r = Object.getOwnPropertySymbols(t),
				e && (r = r.filter((function(e) {
					return Object.getOwnPropertyDescriptor(t, e).enumerable
				}
				))),
				i.push.apply(i, r)),
				i
		}
		function o(t) {
			for (var e = 1; e < arguments.length; e++) {
				var r = null != arguments[e] ? arguments[e] : {};
				e % 2 ? n(Object(r), !0).forEach((function(e) {
					var i, n;
					i = t,
						e = r[n = e],
						n in i ? Object.defineProperty(i, n, {
							value: e,
							enumerable: !0,
							configurable: !0,
							writable: !0
						}) : i[n] = e
				}
				)) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(r)) : n(Object(r)).forEach((function(e) {
					Object.defineProperty(t, e, Object.getOwnPropertyDescriptor(r, e))
				}
				))
			}
			return t
		}
		t.prototype.then = function(e, r) {
			var i = this
				, n = this;
			return "function" != typeof r && (r = function(t) {
				throw t
			}
			),
				"function" != typeof e && (e = function(t) {
					return t
				}
				),
				new t((function(o, s) {
					function h(e) {
						try {
							var r = e(n.PromiseResult);
							r instanceof t ? r.then((function(t) {
								o(t)
							}
							), (function(t) {
								s(t)
							}
							)) : o(r),
								o(r)
						} catch (e) {
							s(e)
						}
					}
					"fulfilled" === i.PromiseState && h(e),
						"rejected" === i.PromiseState && h(r),
						"pending" == i.PromiseState && i.callbacks.push({
							onReject: function() {
								h(r)
							},
							onResolve: function() {
								h(e)
							}
						})
				}
				))
		}
			,
			t.prototype.catch = function(t) {
				return this.then(void 0, t)
			}
			,
			t.resolve = function(e) {
				return new t((function(r, i) {
					try {
						e instanceof t ? e.then((function(t) {
							r(t)
						}
						), (function(t) {
							i(t)
						}
						)) : r(e)
					} catch (t) {
						i(t)
					}
				}
				))
			}
			,
			t.reject = function(e) {
				return new t((function(t, r) {
					r(e)
				}
				))
			}
			,
			t.all = function(e) {
				var r = []
					, i = 0;
				return new t((function(n, o) {
					for (var s = 0; s < e.length; s++)
						!function(s) {
							e[s] instanceof t ? e[s].then((function(t) {
								i++,
									r[s] = t,
									i === e.length && n(r)
							}
							), (function(t) {
								o(t)
							}
							)) : (r[s] = e,
								i++)
						}(s)
				}
				))
			}
			;
		var s, h = t.race = function(e) {
			return new t((function(r, i) {
				for (var n = 0; n < e.length; n++)
					e[n] instanceof t ? e[n].then((function(t) {
						r(t)
					}
					), (function(t) {
						i(t)
					}
					)) : r(e[n])
			}
			))
		}
			, u = null;
		function a() {
			this.handshakePublicKey = "",
				this.handshakeUrl = "",
				this._keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
				this.publicKeyHeader = "",
				this.sm2Key = "",
				this.sm4Key = "",
				this.iv = "",
				this.randomKey = "",
				this.sm2EncryptData = "",
				this.sm4EncryptData = "",
				this.encryptStorageSm4Key = "6c3d6878252e641b",
				this.encryptStorageIv = "5f5e5a247f544d771255134517043757",
				this.encryptRandomKey = "",
				this.encryptSm2RandomKey = "";
			var t = !1
				, e = !1;
			"undefined" != typeof wx && wx.request && wx.login ? t = !0 : "undefined" != typeof jd && jd.request && jd.login ? e = t = !0 : t = !1,
				this.isJd = e,
				t = (this.isApplet = t) ? 2 : 1,
				this.isResponse = !1,
				this.version = [1],
				this.client_type = [t],
				this.key_cipher = [],
				this.time = null,
				this.ms = 6e4,
				this._localStorage = ""
		}
		h = "undefined" != typeof wx && wx.request && wx.login ? (u = wx,
			!0) : !("undefined" == typeof jd || !jd.request || !jd.login || (u = jd,
				0)),
			s = h ? function(e) {
				return new t((function(t, r) {
					u.request(o({
						header: {
							"Content-Type": "application/x-www-form-urlencoded"
						}
					}, e))
				}
				))
			}
				: function(t) {
					(t = t || {}).type = (t.type || "GET").toUpperCase(),
						t.dataType = t.dataType || "json",
						t.async = t.async || !0;
					var e, r = function(t) {
						var e, r = [];
						for (e in t = t || {})
							r.push(encodeURIComponent(e) + "=" + encodeURIComponent(t[e]));
						return r.join("&")
					}(t.data), i = window.XMLHttpRequest ? new XMLHttpRequest : new ActiveXObject("Microsoft.XMLHTTP");
					t.timeout && (e = setTimeout((function() {
						4 != i.readySate && i.abort()
					}
					), t.timeout || 1e4)),
						i.onreadystatechange = function() {
							var r;
							4 == i.readyState && (clearTimeout(e),
								200 <= (r = i.status) && r < 300 || 304 === r ? t.success && t.success(i.responseText, i.responseXML) : t.error && t.error(r))
						}
						,
						"GET" == t.type ? (i.open("GET", t.url + "?" + r, t.async),
							i.send(null)) : "POST" == t.type && (i.open("POST", t.url, t.async),
								i.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"),
								i.send(r))
				}
			,
			a.prototype = {
				commonPromise: function(e, r) {
					var i = this
						, n = 2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : 1
						, o = (r = this.isJd ? encodeURIComponent(r) : r,
							1 !== n ? {
								data: r
							} : {
								clientKey: r
							});
					return new t((function(t, r) {
						var n = {
							url: e,
							method: "POST",
							data: o,
							success: function(e) {
								var i = e.statusCode;
								200 <= i && i < 300 || 304 === i ? t(e.data) : r(i)
							},
							fail: function(t) {
								r(t)
							}
						};
						i.isApplet || (n = {
							type: "POST",
							url: e,
							data: o,
							success: function(e) {
								t(e)
							},
							error: function(t) {
								r(t)
							}
						}),
							s(n)
					}
					))
				},
				encryptDecryptRequest: function(t, e) {
					return this.commonPromise(t, e)
				},
				createDemote: function() {
					this.isResponse || this.demoteKeyCipher()
				},
				demoteKeyCipher: function() {
					var t = [140, 58, 51, 17, 108, 219, 141, 107, 65, 13, 222, 250, 147, 190, 156, 25];
					this.isApplet && (t = [68, 176, 150, 193, 133, 248, 213, 81, 190, 140, 15, 58, 167, 248, 31, 97]);
					var r = this.createRandomKey(8);
					this.randomKey = r;
					var i = this.createRandomKey();
					t = e.sm4.encrypt(r, t, {
						mode: "cbc",
						iv: i
					}),
						this.encryptRandomKey = t,
						t = this.hexToArray(t),
						t = this.hexToArray(i).concat(t, [0, 0, 0, 0, 0]),
						this.key_cipher = t
				},
				handshake: function(t, e) {
					this.isResponse || this.key_cipher.length && Date.now() < this.lastClick + this.ms || (this.handshakeUrl || (this.handshakeUrl = t,
						this.handshakePublicKey = e),
						this.createDemote(),
						this.sm2EncryptRandomKey(t, e))
				},
				encryptRequest: function(t, e) {
					var r = this;
					this.encryptDecryptRequest(t, e).then((function(t) {
						t ? (t = r.decode(t),
							t = Array.prototype.slice.call(t),
							r.key_cipher = t,
							r.isResponse = !0) : (r.isResponse = !1,
								r.lastClick = Date.now())
					}
					)).catch((function(t) {
						r.isResponse = !1,
							r.lastClick = Date.now()
					}
					))
				},
				sm2EncryptRandomKey: function(t, r) {
					var i = e.sm2.doEncrypt(this.randomKey, r)
						, n = this.hexToArray(this.createRandomKey(1))
						, o = this.version;
					r = this.client_type,
						i = this.hexToArray(i),
						i = n.concat(o, r, i),
						i = new Uint8Array(i),
						i = this.arrayBufferToBase64(i),
						this.encryptRequest(t, i)
				},
				createRandomKey: function() {
					var t = this.randomUnit8Array(1, 127, 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : 16);
					return this.buffertoHex(t)
				},
				encrypt: function(t) {
					if (!t)
						throw new Error("encrypt data can not empty");
					this.createDemote();
					var r, i = {
						mode: "cbc",
						iv: r = this.createRandomKey()
					}, n = this.utf8ToHex(this.randomKey), o = e.sm4.encrypt(t, n, i), s = this.hexToArray(o), h = this.hexToArray(this.createRandomKey(1)), u = this.version, a = this.client_type;
					return t = this.isResponse ? [0] : [1],
						n = this.key_cipher,
						i = this.hexToArray(r),
						o = s,
						(r = new Uint32Array(1))[0] = s.length,
						r = Array.prototype.slice.call(new Uint8Array(r.buffer)),
						o = h.concat(u, a, t, n, i, r, o),
						o = new Uint8Array(o),
						o = this.arrayBufferToBase64(o),
						!this.isResponse && this.handshakeUrl && this.handshake(this.handshakeUrl, this.handshakePublicKey),
						o
				},
				encryptData: function(t, e) {
					if (!e)
						throw new Error("encrypt data can not empty");
					var r = (i = this.decode(t)).byteLength
						, i = (t = i.subarray(0, r - 65),
							i.subarray(r - 65));
					return r = this.buffertoHex(t),
						t = this.buffertoHex(i),
						i = this.encryptStorageSm4Data(),
						this.publicKeyHeader = r,
						this.sm2Key = t,
						this.sm4Key = i,
						this.iv = this.createRandomKey(),
						this.encryptSm2Data(),
						this.encryptSm4Data(e),
						this.getEncryptData()
				},
				testDecrpt: function(t, e) {
					return this.commonPromise(t, e, 2)
				},
				test: function(e, r) {
					return this.testDecrpt(e, r).then((function(e) {
						return t.resolve(e)
					}
					)).catch((function(e) {
						return t.reject(e)
					}
					))
				},
				randomUnit8Array: function(t, e, r) {
					e += 1;
					for (var i = [], n = void 0 === r ? 1 : r, o = 0; o < n; o++) {
						var s = Math.floor(Math.random() * (e - t) + t);
						i.push(s)
					}
					return new Uint8Array(i)
				},
				buffertoHex: function(t) {
					return Array.prototype.map.call(t, (function(t) {
						return ("00" + t.toString(16)).slice(-2)
					}
					)).join("")
				},
				encryptSm2Data: function() {
					var t = this.sm4Key
						, r = this.sm2Key;
					r = e.sm2.doEncrypt(t, r),
						this.sm2EncryptData = r
				},
				encryptSm4Data: function(t) {
					var r = this.sm4Key
						, i = {
							mode: "cbc",
							iv: this.iv
						};
					r = this.utf8ToHex(r),
						i = e.sm4.encrypt(t, r, i),
						this.sm4EncryptData = i
				},
				encryptStorageSm4Data: function() {
					var t = this.encryptStorageSm4Key
						, r = {
							mode: "cbc",
							iv: this.encryptStorageIv
						}
						, i = this.utf8ToHex(t)
						, n = ""
						, o = this.isApplet
						, s = this.isJd;
					if (t = o ? s ? jd : wx : null,
						o)
						n = t.getStorageSync("aksKey");
					else
						try {
							n = localStorage.getItem("aksKey")
						} catch (t) {
							n = this._localStorage
						}
					if (s = "",
						n)
						s = e.sm4.decrypt(n, i, r);
					else if (n = this.randomUnit8Array(1, 127, 8),
						s = this.buffertoHex(n),
						r = e.sm4.encrypt(s, i, r),
						o)
						t.setStorageSync("aksKey", r);
					else
						try {
							localStorage.setItem("aksKey", r)
						} catch (t) {
							this._localStorage = r
						}
					return s
				},
				utf8ToHex: function(t) {
					for (var e = (t = unescape(encodeURIComponent(t))).length, r = [], i = 0; i < e; i++)
						r[i >>> 2] |= (255 & t.charCodeAt(i)) << 24 - i % 4 * 8;
					for (var n = [], o = 0; o < e; o++) {
						var s = r[o >>> 2] >>> 24 - o % 4 * 8 & 255;
						n.push((s >>> 4).toString(16)),
							n.push((15 & s).toString(16))
					}
					return n.join("")
				},
				hex2b64: function(t) {
					for (var e, r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", i = "", n = 0; n + 3 <= t.length; n += 3)
						e = parseInt(t.substring(n, n + 3), 16),
							i += r.charAt(e >> 6) + r.charAt(63 & e);
					for (n + 1 == t.length ? (e = parseInt(t.substring(n, n + 1), 16),
						i += r.charAt(e << 2)) : n + 2 == t.length && (e = parseInt(t.substring(n, n + 2), 16),
							i += r.charAt(e >> 2) + r.charAt((3 & e) << 4)); 0 < (3 & i.length);)
						i += "=";
					return i
				},
				leftPad: function(t, e) {
					return t.length >= e ? t : new Array(e - t.length + 1).join("0") + t
				},
				hexToArray: function(t) {
					for (var e = [], r = (t = (r = t.length) % 2 != 0 ? this.leftPad(t, r + 1) : t).length, i = 0; i < r; i += 2)
						e.push(parseInt(t.substr(i, 2), 16));
					return e
				},
				getEncryptData: function() {
					var t = this.hexToArray(this.publicKeyHeader)
						, e = this.hexToArray(this.sm2EncryptData)
						, r = this.hexToArray(this.sm4EncryptData)
						, i = this.hexToArray(this.iv);
					return r = t.concat(e, i, r),
						r = new Uint8Array(r),
						this.arrayBufferToBase64(r)
				},
				removePaddingChars: function(t) {
					return 64 == this._keyStr.indexOf(t.charAt(t.length - 1)) ? t.substring(0, t.length - 1) : t
				},
				arrayBufferToBase64: function(t) {
					for (var e = t.byteLength, r = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"], i = "", n = 0; 3 <= e - n; n += 3) {
						var o = t[n]
							, s = t[n + 1]
							, h = t[n + 2];
						i += r[o >>> 2] + r[(3 & o) << 4 | s >>> 4] + r[(15 & s) << 2 | h >>> 6] + r[63 & h]
					}
					var u, a = e - n;
					return 1 == a ? i += r[(u = t[n]) >>> 2] + r[(3 & u) << 4] + "==" : 2 == a && (u = t[n],
						a = t[n + 1],
						i += r[u >>> 2] + r[(3 & u) << 4 | a >>> 4] + r[(15 & a) << 2] + "="),
						i
				},
				decode: function(t, e) {
					var r = t;
					e = e,
						r = this.removePaddingChars(r),
						r = this.removePaddingChars(r);
					var i, n, o, s, h, u, a = parseInt(r.length / 4 * 3, 10), c = 0, f = 0, p = e ? new Uint8Array(e) : new Uint8Array(a);
					for (r = r.replace(/[^A-Za-z0-9\+\/\=]/g, ""),
						c = 0; c < a; c += 3)
						o = this._keyStr.indexOf(r.charAt(f++)),
							i = (15 & (s = this._keyStr.indexOf(r.charAt(f++)))) << 4 | (h = this._keyStr.indexOf(r.charAt(f++))) >> 2,
							n = (3 & h) << 6 | (u = this._keyStr.indexOf(r.charAt(f++))),
							p[c] = o << 2 | s >> 4,
							64 != h && (p[c + 1] = i),
							64 != u && (p[c + 2] = n);
					return p
				},
				decryptData: function(t) {
					var r = (o = this.decode(t)).byteLength
						, i = o.subarray(3, 19)
						, n = o.subarray(19, r)
						, o = (t = this.buffertoHex(i),
							this.buffertoHex(n));
					if (r = this.isApplet,
						i = "",
						n = this.isJd,
						n = r ? n ? jd : wx : null,
						r)
						try {
							if (!(i = n.getStorageSync("aksKey")))
								throw new Error("get storage fail")
						} catch (t) {
							throw new Error("get storage fail")
						}
					else
						try {
							i = localStorage.getItem("aksKey")
						} catch (t) {
							i = this._localStorage
						}
					if (n = "",
						!i)
						throw new Error("key is invalid");
					return n = this.encryptStorageSm4Data(),
						n = this.utf8ToHex(n),
						e.sm4.decrypt(o, n, {
							mode: "cbc",
							iv: t
						})
				}
			};
		var c = new a
			, f = {
				SummerCryptico: c
			}
		gyx = c;
	}(),
		i
}
));

// var t = 'ARMAclJ6MDAxBMZULdQ8kSzNrFhRJncK0CqKQ9wnC3kSk9UTSdCYlAhsnnIYbab2dMsW+3DOkp8r7C40msi+jTF3jPhZNq/5L54='
// var e = 'uuid=5d481666-5158-4a2f-875b-75a67032c85b&ReturnUrl=https%3A%2F%2Fwww.jd.com%2F&r=0.19618686080775039&version=2015'
// console.log(gyx.encryptData(t, e + ""))
function encrypte(data) {
	var t = 'ARMAclJ6MDAxBMZULdQ8kSzNrFhRJncK0CqKQ9wnC3kSk9UTSdCYlAhsnnIYbab2dMsW+3DOkp8r7C40msi+jTF3jPhZNq/5L54='
	return gyx.encryptData(t, data + "")


}

