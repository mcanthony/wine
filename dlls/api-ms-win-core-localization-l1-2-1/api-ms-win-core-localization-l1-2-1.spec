@ stdcall ConvertDefaultLocale(long) kernel32.ConvertDefaultLocale
@ stdcall EnumSystemGeoID(long long ptr) kernel32.EnumSystemGeoID
@ stdcall EnumSystemLocalesA(ptr long) kernel32.EnumSystemLocalesA
@ stdcall EnumSystemLocalesEx(ptr long long ptr) kernel32.EnumSystemLocalesEx
@ stdcall EnumSystemLocalesW(ptr long) kernel32.EnumSystemLocalesW
@ stub FindNLSString
@ stub FindNLSStringEx
@ stdcall FormatMessageA(long ptr long long ptr long ptr) kernel32.FormatMessageA
@ stdcall FormatMessageW(long ptr long long ptr long ptr) kernel32.FormatMessageW
@ stdcall GetACP() kernel32.GetACP
@ stdcall GetCPInfo(long ptr) kernel32.GetCPInfo
@ stdcall GetCPInfoExW(long long ptr) kernel32.GetCPInfoExW
@ stdcall GetCalendarInfoEx(wstr long ptr long ptr long ptr) kernel32.GetCalendarInfoEx
@ stdcall GetCalendarInfoW(long long long ptr long ptr) kernel32.GetCalendarInfoW
@ stdcall GetFileMUIInfo(long wstr ptr ptr) kernel32.GetFileMUIInfo
@ stdcall GetFileMUIPath(long wstr wstr ptr ptr ptr ptr) kernel32.GetFileMUIPath
@ stdcall GetGeoInfoW(long long ptr long long) kernel32.GetGeoInfoW
@ stdcall GetLocaleInfoA(long long ptr long) kernel32.GetLocaleInfoA
@ stdcall GetLocaleInfoEx(wstr long ptr long) kernel32.GetLocaleInfoEx
@ stdcall GetLocaleInfoW(long long ptr long) kernel32.GetLocaleInfoW
@ stub GetNLSVersion
@ stub GetNLSVersionEx
@ stdcall GetOEMCP() kernel32.GetOEMCP
@ stub GetProcessPreferredUILanguages
@ stdcall GetSystemDefaultLCID() kernel32.GetSystemDefaultLCID
@ stdcall GetSystemDefaultLangID() kernel32.GetSystemDefaultLangID
@ stub GetSystemPreferredUILanguages
@ stdcall GetThreadLocale() kernel32.GetThreadLocale
@ stdcall GetThreadPreferredUILanguages(long ptr ptr ptr) kernel32.GetThreadPreferredUILanguages
@ stdcall GetThreadUILanguage() kernel32.GetThreadUILanguage
@ stub GetUILanguageInfo
@ stdcall GetUserDefaultLCID() kernel32.GetUserDefaultLCID
@ stdcall GetUserDefaultLangID() kernel32.GetUserDefaultLangID
@ stdcall GetUserDefaultLocaleName(ptr long) kernel32.GetUserDefaultLocaleName
@ stdcall GetUserGeoID(long) kernel32.GetUserGeoID
@ stdcall GetUserPreferredUILanguages(long ptr ptr ptr) kernel32.GetUserPreferredUILanguages
@ stdcall IdnToAscii(long wstr long ptr long) kernel32.IdnToAscii
@ stdcall IdnToUnicode(long wstr long ptr long) kernel32.IdnToUnicode
@ stdcall IsDBCSLeadByte(long) kernel32.IsDBCSLeadByte
@ stdcall IsDBCSLeadByteEx(long long) kernel32.IsDBCSLeadByteEx
@ stub IsNLSDefinedString
@ stdcall IsValidCodePage(long) kernel32.IsValidCodePage
@ stdcall IsValidLanguageGroup(long long) kernel32.IsValidLanguageGroup
@ stdcall IsValidLocale(long long) kernel32.IsValidLocale
@ stdcall IsValidLocaleName(wstr) kernel32.IsValidLocaleName
@ stub IsValidNLSVersion
@ stdcall LCMapStringA(long long str long ptr long) kernel32.LCMapStringA
@ stdcall LCMapStringEx(wstr long wstr long ptr long ptr ptr long) kernel32.LCMapStringEx
@ stdcall LCMapStringW(long long wstr long ptr long) kernel32.LCMapStringW
@ stdcall LocaleNameToLCID(wstr long) kernel32.LocaleNameToLCID
@ stub ResolveLocaleName
@ stdcall SetCalendarInfoW(long long long wstr) kernel32.SetCalendarInfoW
@ stdcall SetLocaleInfoW(long long wstr) kernel32.SetLocaleInfoW
@ stub SetProcessPreferredUILanguages
@ stdcall SetThreadLocale(long) kernel32.SetThreadLocale
@ stdcall SetThreadPreferredUILanguages(long ptr ptr) kernel32.SetThreadPreferredUILanguages
@ stdcall SetThreadUILanguage(long) kernel32.SetThreadUILanguage
@ stdcall SetUserGeoID(long) kernel32.SetUserGeoID
@ stdcall VerLanguageNameA(long str long) kernel32.VerLanguageNameA
@ stdcall VerLanguageNameW(long wstr long) kernel32.VerLanguageNameW
