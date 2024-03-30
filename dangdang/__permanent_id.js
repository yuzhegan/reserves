
var crypto = require('crypto-js');

function createPermanentID() {
	var n = new Date();
	// console.log("n===>", n)
	var y = n.getFullYear() + '';
	var m = n.getMonth() + 1;
	if (m < 10)
		m = "0" + m;
	var d = n.getDate();
	if (d < 10)
		d = "0" + d;
	var H = n.getHours();
	if (H < 10)
		H = "0" + H;
	var M = n.getMinutes();
	if (M < 10)
		M = "0" + M;
	var S = n.getSeconds();
	if (S < 10)
		S = "0" + S;
	var a = "00" + n.getMilliseconds();
	a = a.substr(a.length - 3, 3);
	var b = Math.floor(100000 + Math.random() * 900000);
	var c = Math.floor(100000 + Math.random() * 900000);
	var e = y + m + d + H + M + S + a + b + c + "DDClick521";
	// var f = k.Md5Util.hex_md5(e);
	var f = crypto.MD5(e).toString(crypto.enc.Hex);
	// console.log(f)
	f = formatHashCode(f);
	return y + m + d + H + M + S + a + f + b + c
};
formatHashCode = function(a) {
	var b = parseInt(String(a).substr(0, 8), 16);
	var c = String(b).substr(0, 6);
	var d = c.length;
	if (d < 6) {
		c += k.str_repeat('0', Math.abs(6 - d))
	}
	return c
}
// console.log(createPermanentID())
