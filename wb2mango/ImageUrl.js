function constructHostV2(e, t = "nm") {
	const r = parseInt(e, 10)
		, n = ~~(r / 1e5)
		, a = ~~(r / 1e3);
	return `https://${"nm" === t ? volHostV2(n) : volFeedbackHost(n)}`
}

function volFeedbackHost(e) {
	let t;
	switch (!0) {
		case e >= 0 && e <= 431:
			t = "01";
			break;
		case e >= 432 && e <= 863:
			t = "02";
			break;
		case e >= 864 && e <= 1199:
			t = "03";
			break;
		case e >= 1200 && e <= 1535:
			t = "04";
			break;
		case e >= 1536 && e <= 1919:
			t = "05";
			break;
		default:
			t = "06"
	}
	return `feedback ${t}.wbbasket.ru`
}

function volHostV2(e) {
	let t;
	switch (!0) {
		case e >= 0 && e <= 143:
			t = "01";
			break;
		case e >= 144 && e <= 287:
			t = "02";
			break;
		case e >= 288 && e <= 431:
			t = "03";
			break;
		case e >= 432 && e <= 719:
			t = "04";
			break;
		case e >= 720 && e <= 1007:
			t = "05";
			break;
		case e >= 1008 && e <= 1061:
			t = "06";
			break;
		case e >= 1062 && e <= 1115:
			t = "07";
			break;
		case e >= 1116 && e <= 1169:
			t = "08";
			break;
		case e >= 1170 && e <= 1313:
			t = "09";
			break;
		case e >= 1314 && e <= 1601:
			t = "10";
			break;
		case e >= 1602 && e <= 1655:
			t = "11";
			break;
		case e >= 1656 && e <= 1919:
			t = "12";
			break;
		case e >= 1920 && e <= 2045:
			t = "13";
			break;
		case e >= 2046 && e <= 2189:
			t = "14";
			break;
		default:
			t = "15"
	}
	return `basket-${t}.wbbasket.ru`
}


// console.log(constructHostV2("34659218"));
