// var crypto = require('crypto');
var crypto = require('crypto-js');


// t = new Date().getTime().toString()
// var a = 'ct=pc&permanent_id=20230928230455514270999263474133549&t=' + t
// var a = 'ct=pc&permanent_id=20230929070817084372090583039556965&t=1695942982810'
// console.log(a)
// a = Y(a)  //Y(a) md5
// a 为需要md5的明文参数 到python里面处理
// permanent_id 为cookies生成的 _permanent_id 的value
function AesEncrypt(a, rankey) {
	// var a = crypto.MD5(a).toString()
	// console.log(a)
	H = crypto.enc.Utf8.parse("0102030405060708")
	J = function(t, e) {
		e = crypto.enc.Utf8.parse(e);
		var n = crypto.enc.Utf8.parse(t);
		return crypto.AES.encrypt(n, e, {
			iv: H
		}).toString()
	};
	resulat = J(a, rankey);
	return resulat
};


// console.log(AesEncrypt('{"x":0.7628571428571429,"y":0.1127451}', 'Wg1mNDiK31VMsB9G'))
// console.log(AesEncrypt(267,0.1127451, 'Wg1mNDiK31VMsB9G'))


