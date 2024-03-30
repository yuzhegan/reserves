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
	var a = crypto.MD5(a).toString()
	console.log(a)

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


console.log(AesEncrypt('ct=pc&need_new_verifydata=0&permanent_id=20231003144836115164138128881944335&point_json=aWr1tTpulziQcKFJVM8dE1Qjnxhf0oYn9Wn1Hm+SV1q18zaztw75iOwz/jQDvWvc=&requestId=2310031448265340D8vR4n_30eb&situation=login&slide_cost_time=2121&t=1696315717472&verifyToken=eabc20c65d694d97b15c695324292715', 'PgYnTTwaapDf2nZV'))


