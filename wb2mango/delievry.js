
function dateFromTimestamp(t, e) {
    return new Date(t).format(e || "dd.MM.yyyy HH:mm")
}

function deliveryDateTxt(t) {
    if (!t || "number" != typeof t)
        return "";
    let e;
    const r = new Date(Date.now())
      , n = new Date(r.getTime() + 60 * t * 60 * 1e3);
    n.is1stJan() && (n.setDate(n.getDate() + 1),
    t += 24);
    const o = 24 - r.getHours()
      , i = n.getHours();
    return r.getDate() === n.getDate() && t < 24 ? e = i < 9 ? "сегодня утром" : i < 23 ? $.pluralize(t, "{0} час", "{0} часа", "{0} часов") : "завтра утром" : t < o + 9 ? e = "завтра утром" : t < 24 + o ? e = i < 23 ? "завтра" : "послезавтра" : t < 48 + o && i < 23 ? e = "послезавтра" : (i >= 23 && (t += o),
    e = dateFromTimestamp(Date.now() + 60 * t * 60 * 1e3, "d MMMM")),
    e
}

Date.prototype.is1stJan = function() {
    return 1 === this.getDate() && 0 === this.getMonth()
}



var localizedfr = {
    "abbreviatedDayNames": ["вс", "пн", "вт", "ср", "чт", "пт", "сб"],
    "dayNames": ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"],
    "monthNames": ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"],
    "abbreviatedMonthNames": ["янв", "февр", "марта", "апр", "мая", "июня", "июля", "авг", "сент", "окт", "нояб", "дек"],
    "monthGenitiveNames": ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
}

Date.prototype.format = function(t, e) {
    var a, n, i, o, s = (a = /d{1,4}|M{1,5}|yy(?:yy)?|([HhmsTt])\1?|[LloSZ]|"[^"]*"|'[^']*'/g,
    n = /\b(?:[PMCEA][SDP]T|(?:Pacific|Mountain|Central|Eastern|Atlantic) (?:Standard|Daylight|Prevailing) Time|(?:GMT|UTC)(?:[-+]\d{4})?)\b/g,
    i = /[^-+\dA-Z]/g,
    o = function(t, e) {
        for (t = String(t),
        e = e || 2; t.length < e; )
            t = "0" + t;
        return t
    }
    ,
    function(t, e, r) {
        var d = s;
        if (1 != arguments.length || "[object String]" != Object.prototype.toString.call(t) || /\d/.test(t) || (e = t,
        t = void 0),
        t = t ? new Date(t) : new Date,
        isNaN(t))
            throw SyntaxError("invalid date");
        "UTC:" == (e = String(d.masks[e] || e || d.masks.default)).slice(0, 4) && (e = e.slice(4),
        r = !0);
        var m = r ? "getUTC" : "get"
          , l = t[m + "Date"]()
          , M = t[m + "Day"]()
          , y = t[m + "Month"]()
          , h = t[m + "FullYear"]()
          , u = t[m + "Hours"]()
          , c = t[m + "Minutes"]()
          , f = t[m + "Seconds"]()
          , g = t[m + "Milliseconds"]()
          , D = r ? 0 : t.getTimezoneOffset()
          , T = {
            d: l,
            dd: o(l),
            ddd: d.i18n.dayNames[M],
            dddd: d.i18n.dayNames[M + 7],
            M: y + 1,
            MM: o(y + 1),
            MMM: d.i18n.monthNames[y],
            MMMM: d.i18n.monthNames[y + 12],
            MMMMM: d.i18n.monthNames[y + 24],
            yy: String(h).slice(2),
            yyyy: h,
            h: u % 12 || 12,
            hh: o(u % 12 || 12),
            H: u,
            HH: o(u),
            m: c,
            mm: o(c),
            s: f,
            ss: o(f),
            l: o(g, 3),
            L: o(g > 99 ? Math.round(g / 10) : g),
            t: u < 12 ? "a" : "p",
            tt: u < 12 ? "am" : "pm",
            T: u < 12 ? "A" : "P",
            TT: u < 12 ? "AM" : "PM",
            Z: r ? "UTC" : (String(t).match(n) || [""]).pop().replace(i, ""),
            o: (D > 0 ? "-" : "+") + o(100 * Math.floor(Math.abs(D) / 60) + Math.abs(D) % 60, 4),
            S: ["th", "st", "nd", "rd"][l % 10 > 3 ? 0 : (l % 100 - l % 10 != 10) * l % 10]
        };
        return e.replace(a, function(t) {
            return t in T ? T[t] : t.slice(1, t.length - 1)
        })
    }
    );
    return s.masks = {
        default: "ddd mmm dd yyyy HH:MM:ss",
        shortDate: "m/d/yy",
        mediumDate: "mmm d, yyyy",
        longDate: "mmmm d, yyyy",
        fullDate: "dddd, mmmm d, yyyy",
        shortTime: "h:MM TT",
        mediumTime: "h:MM:ss TT",
        longTime: "h:MM:ss TT Z",
        isoDate: "yyyy-mm-dd",
        isoTime: "HH:MM:ss",
        isoDateTime: "yyyy-mm-dd'T'HH:MM:ss",
        isoUtcDateTime: "UTC:yyyy-mm-dd'T'HH:MM:ss'Z'"
    },
    s.i18n = {
        dayNames: ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"],
        monthNames: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    },
    localizedfr && (s.i18n.dayNames = localizedfr.abbreviatedDayNames.concat(localizedfr.dayNames),
    localizedfr.abbreviatedMonthNames[1] = "февр",
    localizedfr.abbreviatedMonthNames[2] = "марта",
    localizedfr.abbreviatedMonthNames[4] = "мая",
    localizedfr.abbreviatedMonthNames[5] = "июня",
    localizedfr.abbreviatedMonthNames[6] = "июля",
    localizedfr.abbreviatedMonthNames[8] = "сент",
    localizedfr.abbreviatedMonthNames[10] = "нояб",
    s.i18n.monthNames = localizedfr.abbreviatedMonthNames.concat(localizedfr.monthGenitiveNames).concat(localizedfr.monthNames.map(([t,...e])=>t.toUpperCase() + e.join("")))),
    s(this, t, e)
}

// console.log(deliveryDateTxt(136))
