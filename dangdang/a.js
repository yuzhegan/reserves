// config AES 加密函数
var CryptoJS = require("crypto-js");
// 加密
 
// var str = '17fdabf4e351319ec7c5e5103d54daa3';
// 密钥 16 位
// var key = 'seqLuMppJOLCorlm'

// 初始向量 initial vector 16 位
// var iv = '0102030405060708';
// key 和 iv 可以一致
 
function GenAesString(data, key, iv) {
	key = CryptoJS.enc.Utf8.parse(key);
	iv = CryptoJS.enc.Utf8.parse(iv);
	 
	var encrypted = CryptoJS.AES.encrypt(data, key, {
			iv: iv,
			mode: CryptoJS.mode.CBC,
			padding: CryptoJS.pad.Pkcs7
	});
	return encrypted.toString(); // 返回的是base64格式的密文
	// encrypted = encrypted.toString();
}
 
// 转换为字符串
// console.log(encrypted);
 
// mode 支持 CBC、CFB、CTR、ECB、OFB, 默认 CBC
// padding 支持 Pkcs7、AnsiX923、Iso10126
// NoPadding、ZeroPadding, 默认 Pkcs7, 即 Pkcs5
 
// 解密
// var decrypted = CryptoJS.AES.decrypt(encrypted, key, {
//     iv: iv,
//     mode: CryptoJS.mode.CBC,
//     padding: CryptoJS.pad.Pkcs7
// });
 
// 转换为 utf8 字符串
// decrypted = CryptoJS.enc.Utf8.stringify(decrypted);
