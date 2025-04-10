# 코드 통합본
id = "다예"
home = "서울"
young = "N"
subsidiary = "N"
payment = 1700
start_point = "경복궁역2번출구"
end_point = "총신대입구역.남성사계시장입구앞"
transport = ["7016","502"] 
# 이동 횟수 : 4~5주 (20~25일 -> 40~50회)
# min : 40, max : 50


# 기후동행카드 가능 범위
class Area:
    # 가능 지하철역
    stations = [
    "온수", "오류동", "개봉", "구일", "구로", "신도림", "영등포", "신길", "대방", "노량진", "용산", "남영", 
    "서울역", "시청", "종각", "종로3가", "종로5가", "동대문", "동묘앞", "신설동", "제기동", "청량리", "회기", 
    "외대앞", "신이문", "석계", "광운대", "월계", "녹천", "창동", "방학", "도봉", "도봉산", "건대입구", 
    "구의", "강변", "잠실나루", "잠실", "잠실새내", "종합운동장", "삼성", "선릉", "역삼", "강남", "교대", 
    "서초", "방배", "사당", "낙성대", "서울대입구", "봉천", "신림", "신대방", "구로디지털단지", "대림", 
    "신도림", "문래", "영등포구청", "당산", "합정", "홍대입구", "신촌", "이대", "아현", "충정로", "시청", 
    "을지로입구", "을지로3가", "을지로4가", "동대문역사문화공원", "신당", "상왕십리", "왕십리", "한양대", 
    "뚝섬", "성수", "용답", "마장", "신답", "용두", "신설동", "도림천", "양천구청", "신정네거리", "까치산", 
    "오금", "경찰병원", "문정", "가락시장", "수서", "일원", "대청", "학여울", "대치", "도곡", "매봉", 
    "양재", "남부터미널", "교대", "고속터미널", "잠원", "신사", "압구정", "옥수", "금호", "약수", "동대입구", 
    "충무로", "을지로3가", "종로3가", "안국", "경복궁", "독립문", "무악재", "홍제", "녹번", "불광", "연신내", 
    "구파발", "지축", "남태령", "사당", "총신대입구(이수)", "동작", "이촌", "신용산", "삼각지", "숙대입구", 
    "서울역", "회현", "명동", "충무로", "동대문역사문화공원", "동대문", "혜화", "한성대입구", "성신여대입구", 
    "길음", "미아사거리", "미아", "수유", "쌍문", "창동", "노원", "상계", "당고개", "방화", "개화산", 
    "김포공항", "송정", "마곡", "발산", "우장산", "화곡", "까치산", "신정", "목동", "오목교", "양평", 
    "영등포구청", "영등포시장", "신길", "여의도", "여의나루", "마포", "공덕", "애오개", "충정로", "서대문", 
    "광화문", "을지로3가", "을지로4가", "동대문역사문화공원", "청구", "신금호", "행당", "왕십리", "마장", 
    "답십리", "장한평", "군자", "아차산", "광나루", "천호", "강동", "둔촌동", "올림픽공원", "방이", "오금", 
    "개롱", "거여", "마천", "길동", "굽은다리", "명일", "고덕", "상일동", "강일", "신내", "봉화산", "화랑대", 
    "태릉입구", "석계", "돌곶이", "상월곡", "월곡", "고려대", "안암", "창신", "신당", "청구", "약수", 
    "버티고개", "한강진", "이태원", "녹사평", "삼각지", "효창공원앞", "대흥", "광흥창", "상수", "합정", 
    "망원", "마포구청", "월드컵경기장", "디지털미디어시티", "증산", "새절", "응암", "역촌", "불광", "독바위", 
    "구산", "장암", "도봉산", "수락산", "마들", "노원", "중계", "하계", "공릉", "태릉입구", "먹골", 
    "중화", "상봉", "면목", "사가정", "용마산", "중곡", "군자", "어린이대공원", "건대입구", "뚝섬유원지", 
    "청담", "강남구청", "학동", "논현", "반포", "고속터미널", "내방", "총신대입구(이수)", "남성", "숭실대입구", 
    "상도", "장승배기", "신대방삼거리", "보라매", "대림", "남구로", "가산디지털단지", "철산", "광명사거리", 
    "천왕", "온수", "암사", "천호", "강동구청", "몽촌토성", "잠실", "석촌", "송파", "가락시장", "문정", 
    "장지", "복정", "남위례", "산성", "남한산성입구", "단대오거리", "신흥", "수진", "모란", "중앙보훈병원", 
    "둔촌오륜", "올림픽공원", "한성백제", "송파나루", "석촌", "석촌고분", "삼전", "봉은사", "삼성중앙", 
    "선정릉", "언주", "신논현", "사평", "고속터미널", "신반포", "구반포", "동작", "노량진", "샛강", 
    "여의도", "국회의사당", "당산", "선유도", "신목동", "염창", "등촌", "증미", "가양", "양천향교", 
    "마곡나루", "신방화", "공항시장", "김포공항", "개화", "고촌", "풍무", "사우", "걸포북변", "운양", 
    "장기", "마산", "구래", "양촌", "수색", "디지털미디어시티", "가좌", "신촌(경의중앙선)", "서울역", 
    "홍대입구", "서강대", "공덕", "효창공원앞", "용산", "이촌", "서빙고", "한남", "옥수", "응봉", "행당", 
    "청량리", "회기", "중랑", "상봉", "망우", "양원", "망우", "상봉", "신내", "중랑", "청량리", "회기", 
    "김포공항", "마곡나루", "디지털미디어시티", "홍대입구", "공덕", "서울역", "소사", "소새울", "시흥대야", 
    "신천", "신현", "시흥시청", "시흥능곡", "달미", "선부", "초지", "안산", "원곡", "원시", "청량리", 
    "왕십리", "서울숲", "압구정로데오", "강남구청", "선정릉", "선릉", "한티", "도곡", "구룡", "개포동", 
    "대모산입구", "수서", "복정", "관악산", "서울대벤처타운", "서원", "신림", "당곡", "보라매병원", "보라매공원", 
    "보라매", "서울지방병무청", "대방", "샛강", "북한산우이", "솔밭공원", "4.19민주묘지", "가오리", "화계", 
    "삼양", "삼양사거리", "솔샘", "북한산보국문", "정릉", "성신여대입구", "보문", "신설동"
    ]
    # 가능 버스 번호
    bus_routes = [
    "0017", "01A", "01B", "0411", "100", "101", "1014", "1017", "102", "1020", "103", "104", "105", "106", "107", 
    "109", "110", "111", "1112", "1113", "1114", "1115", "1116", "1119", "1120", "1122", "1124", "1126", "1127", 
    "1128", "1129", "1130", "1131", "1132", "1133", "1135", "1136", "1137", "1138", "1139", "1140", "1141", "1142", 
    "1143", "1144", "1154", "1155", "1162", "1164", "1165", "1167", "120", "121", "1213", "1218", "1221", "1222", 
    "1224", "1226", "1227", "130", "140", "141", "142", "143", "144", "145", "146", "147", "148", "150", "151", 
    "152", "160", "162", "163", "171", "1711", "172", "173", "201", "2012", "2013", "2014", "2015", "2016", "202", 
    "2112", "2113", "2114", "2115", "2211", "2212", "2221", "2222", "2224", "2227", "2230", "2233", "2236", "2311", 
    "2312", "240", "241", "2412", "2413", "2415", "2416", "242", "260", "261", "262", "270", "271", "272", "273", 
    "301", "3011", "302", "303", "320", "3212", "3214", "3216", "3217", "3220", "3313", "3314", "3315", "3316", 
    "3317", "3318", "3319", "3321", "3322", "3323", "333", "340", "341", "3411", "3412", "3413", "3414", "3416", 
    "3417", "342", "3420", "3422", "3426", "343", "345", "350", "360", "361", "370", "400", "401", "402", "405", 
    "406", "420", "421", "4211", "4212", "422", "4312", "4318", "4319", "440", "441", "4425", "4432", "4433", 
    "4435", "452", "461", "463", "470", "472", "500", "501", "5012", "502", "503", "504", "505", "506", "507", 
    "540", "541", "5413", "542", "5511", "5513", "5515", "5516", "5517", "5519", "5522", "5523", "5524", "5525", 
    "5528", "5530", "5531", "5535", "5536", "5537", "5611", "5615", "5616", "5617", "5618", "5619", "5620", "5621", 
    "5623", "5625", "5626", "5627", "5630", "5633", "5634", "571", "5712", "5713", "5714", "600", "601", "602", 
    "603", "604", "605", "606", "6211", "640", "641", "6411", "643", "650", "651", "6511", "6512", "6514", "6515", 
    "6516", "652", "653", "654", "660", "661", "6613", "6614", "6615", "6616", "6617", "662", "6620", "6623", 
    "6624", "6625", "6627", "6628", "6629", "6630", "6631", "6632", "6633", "6637", "6638", "6640", "6642", "6645", 
    "6647", "6648", "6657", "6712", "6713", "6714", "6715", "6716", "672", "673", "674", "700", "701", "7011", 
    "7013", "7016", "7017", "7018", "7019", "702", "7021", "7022", "7024", "7025", "703", "704", "705", "707", 
    "708", "710", "720", "721", "7211", "7212", "740", "741", "742", "750", "752", "753", "760", "761", "7611", 
    "7612", "7613", "771", "7711", "7713", "7715", "7719", "7720", "7722", "7723", "7726", "7727", "7728", "773", 
    "7730", "7734", "7737", "7738", "7739", "774", "8002", "8003", "8101", "8146", "8221", "8331", "8441", "8541", 
    "8551", "8552", "8561", "8641", "8701", "8762", "8771", "8772", "8773", "8774", "8777", "N13", "N15", "N16", 
    "N26", "N30", "N31", "N37", "N51", "N61", "N62", "N64", "N72", "N73", "N75", "강남01", "강남02", "강남03", 
    "강남05", "강남06", "강남06-1", "강남06-2", "강남07", "강남08", "강남10", "강동01", "강동02", "강동05", "강북01", 
    "강북02", "강북03", "강북04", "강북05", "강북06", "강북08", "강북09", "강북10", "강북11", "강북12", "강서01", 
    "강서02", "강서02", "강서03", "강서04", "강서05", "강서05-1", "강서06", "강서07", "관악01", "관악02", "관악03", 
    "관악04", "관악05", "관악06", "관악07", "관악07", "관악08", "관악08", "관악10", "관악11", "광진01", "광진02", 
    "광진03", "광진04", "광진05", "구로01", "구로02", "구로03", "구로04", "구로05", "구로06", "구로07", "구로08", 
    "구로09", "구로10", "구로11", "구로12", "구로13", "구로14", "구로15", "금천01", "금천02", "금천03", "금천04", 
    "금천05", "금천06", "금천07", "금천08", "금천11", "노원01", "노원02", "노원03", "노원05", "노원08", "노원09", 
    "노원11", "노원13", "노원14", "노원15", "도봉01", "도봉02", "도봉03", "도봉04", "도봉05", "도봉06", "도봉07", 
    "도봉08", "도봉09", "동대문01", "동대문02", "동대문03", "동대문05", "동작01", "동작02", "동작03", "동작05", 
    "동작05-1", "동작06", "동작07", "동작08", "동작09", "동작10", "동작11", "동작12", "동작13", "동작14", "동작15", 
    "동작16", "동작17", "동작18", "동작19", "동작20", "동작21", "동행버스 서울02", "동행버스 서울04", "동행버스 서울05", 
    "동행버스 서울07", "동행버스 서울07", "동행버스 서울08", "동행버스 서울09", "동행버스 서울10", "마포01", 
    "마포02", "마포03", "마포05", "마포06", "마포07", "마포08", "마포09", "마포10", "마포11", "마포12", "마포13", 
    "마포15", "마포16", "마포17", "마포18", "마포18-1", "서대문01", "서대문02", "서대문03", "서대문04", "서대문05", 
    "서대문06", "서대문07", "서대문08", "서대문09", "서대문10", "서대문11", "서대문12", "서대문13", "서대문14", 
    "서대문15", "서울02", "서울04", "서울05", "서초01", "서초02", "서초03", "서초05", "서초06", "서초07", "서초08", 
    "서초09", "서초10", "서초11", "서초13", "서초14", "서초15", "서초16", "서초17", "서초18", "서초18", 
    "서초18-1", "서초18-1", "서초20", "서초21", "서초22", "성동01", "성동02", "성동03-1", "성동03-2", "성동05", 
    "성동08", "성동09", "성동10", "성동12", "성동13", "성동14", "성동15", "성북01", "성북02", "성북03", "성북04", 
    "성북05", "성북06", "성북07", "성북08", "성북09", "성북10", "성북12", "성북13", "성북14-1", "성북14-2", 
    "성북15", "성북20", "성북21", "성북22", "송파01", "송파02", "송파03", "양천01", "양천02", "양천03", "양천04", 
    "영등포01", "영등포02", "영등포03", "영등포04", "영등포05", "영등포06", "영등포07", "영등포08", "영등포09", 
    "영등포10", "영등포11", "영등포12", "영등포13", "용산01", "용산02", "용산03", "용산04", "은평02", "은평03", 
    "은평04", "은평05", "은평06", "은평07", "은평08-1", "은평08-2", "은평09", "은평10", "종로01", "종로02", 
    "종로03", "종로05", "종로06", "중구01", "중구02", "중구03", "중구04", "중구05", "중구06", "중구07", "중랑01", 
    "중랑02", "중랑03", "중랑04", "중랑05"
    ]

    # 노선 체크 함수
    @classmethod    
    def check(cls, station):
        if station in cls.stations or station in cls.bus_routes :
            return "Y"
        else :
            return "N"


# 교통비 계산
class Card:
    def __init__(self) :
        self.min = 40
        self.max = 50
        

    # 일반 교통비 함수
    def original(self, payment):
        result = []

        for num_moves in (self.min, self.max) :
            result.append(payment * num_moves) 
        return result
    

    # 기후동행카드 교통비 함수
    def gidongca(self, start_point, end_point, young):
        result = []
        # 기후동행카드 사용 가능 영역
        if Area.check(start_point) == "Y" and Area.check(end_point) == "Y" or all(bus in Area.bus_routes for bus in transport) == True:
            # 청년(따릉이 미포함, 포함)
            if young == "Y":
                result.append(55000) 
                result.append(58000) 
            # 일반(따릉이 미포함, 포함)
            else:
                result.append(62000) 
                result.append(65000) 
            return result
        
        # 기후동행카드 사용 불가 영역
        else :  
            return "k_pass"


    # K-패스 교통비 함수
    def k_pass(self, payment, subsidiary, young):
        result = []

        for num_moves in (self.min, self.max) :
            # 일반 교통비
            original = payment * num_moves

            # 이동 횟수 미충족(15회 미만)
            if num_moves < 15:
                cal = original

            # 이동 횟수 충족(15회 이상, 60회 이하)
            elif num_moves <= 60:
                # 20만원 이하
                if original <= 200000:
                    # 저소득층
                    if subsidiary == "Y":
                        cal = original * (1 - 0.53)
                    # 청년
                    elif young == "Y":
                        cal = original * (1 - 0.3)
                    # 일반
                    else:
                        cal = original * (1 - 0.2)
                # 20만원 초과 (초과 비용에 대해서는 절반만 혜택 적용)
                else:
                    # 저소득층 
                    if subsidiary == "Y":
                        cal = original - (200000 + (original - 200000) / 2) * 0.53
                    # 청년
                    elif young == "Y":
                        cal = original - (200000 + (original - 200000) / 2) * 0.3
                    # 일반
                    else:
                        cal = original - (200000 + (original - 200000) / 2) * 0.2

            # 이동 횟수 초과(60회 이상)
            else:
                # 20만원 이하 
                if original <= 200000:
                    # 저소득층
                    if subsidiary == "Y":
                       cal = (payment * 60) * (1 - 0.53) + payment * (num_moves - 60)
                    # 청년
                    elif young == "Y":
                        cal = (payment * 60) * (1 - 0.3) + payment * (num_moves - 60)
                    # 일반
                    else:
                        cal = (payment * 60) * (1 - 0.2) + payment * (num_moves - 60)
                # 20만원 초과
                else:
                    # 저소득층
                    if subsidiary == "Y":
                       cal = (payment * 60) * (1 - 0.53) + payment * (num_moves - 60)
                       cal = original - (200000 + (result - 200000) / 2) * 0.53
                    # 청년
                    elif young == "Y":
                        cal = (payment * 60) * (1 - 0.3) + payment * (num_moves - 60)
                        cal = original - (200000 + (result - 200000) / 2) * 0.3
                    # 일반
                    else:
                        cal = (payment * 60) * (1 - 0.2) + payment * (num_moves - 60)
                        cal = original - (200000 + (result - 200000) / 2) * 0.2
            result.append(round(cal))

        return result



    # The경기패스, 인천I패스 교통비 함수
    def k_pass_plus(self, payment, subsidiary, young) :
        result = []

        for num_moves in (self.min, self.max) :
            # 일반 교통비
            original = payment * num_moves

            # 15회 미만
            if num_moves < 15 :
                cal = original

            # 15회 이상  
            else :
                # 저소득층
                if subsidiary == "Y" :
                    cal = original * (1 - 0.53)
                # 청년층
                elif young == "Y" :
                    cal = original * (1 - 0.3)
                # 일반층
                else :
                    cal = original * (1 - 0.2)
            result.append(round(cal))

        return result

    
# K-패스 카드 23개 "추가" 할인
class Discount:

    def __init__(self, k_pass) :
        self.k_pass = k_pass
        card = Card()
        self.min = card.min
        self.max = card.max

    # BC 바로카드 (신용, 후불, 실물) | K-패스 카드 
    def bc_credit(self, pre_month):
        discount_result = []

        for k_pass_price in self.k_pass :
            # 이전 달, 100만원 이상 사용
            if pre_month >= 1000000 :
                cal = min(k_pass_price * 0.15, 15000)
            # 이전 달, 60만원 이상 사용
            elif pre_month >= 600000 :
                cal = min(k_pass_price * 0.15, 12000)
            # 이전 달, 30만원 이상 사용
            elif pre_month >= 300000 :
                cal = min(k_pass_price * 0.15, 7000)
            # 이전 달, 실적 미충족
            else :
                cal = 0
            discount_result.append(round(cal))

        return discount_result
    

    # 신한카드 (신용, 후불, 모바일) | 티머니 Pay & GO 신한카드 
    def shinhan_credit_tmoney(self, pre_month):
        discount_result_mobile = []
        discount_result_go = []

        # 모바일 티머니 (IPone X), 티머니 GO
        for k_pass_price in self.k_pass :
            # 이전 달, 100만원 이상 사용
            if pre_month >= 1000000 :
                cal_mobile = min(k_pass_price * 0.3, 18000)
                cal_go = min(k_pass_price * 0.2, 18000)
            # 이전 달, 50만원 이상 사용
            elif pre_month >= 500000 :
                cal_mobile = min(k_pass_price * 0.3, 12000)
                cal_go = min(k_pass_price * 0.2, 12000)
            # 이전 달, 30만원 이상 사용
            elif pre_month >= 300000 :
                cal_mobile = min(k_pass_price * 0.3, 7000)
                cal_go = min(k_pass_price * 0.2, 7000)
            # 이전 달, 실적 미충족
            else :
                cal_mobile = 0
                cal_go = 0
        
            discount_result_mobile.append(round(cal_mobile))
            discount_result_go.append(round(cal_go))

        return discount_result_mobile, discount_result_go


    # 신한카드 (신용, 후불, 실물) | K-패스 신한카드 
    def sinhan_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass :
            # 이전 달, 60만원 이상 사용
            if pre_month >= 600000:
                cal =  min(k_pass_price * 0.1, 15000)
            # 이전 달, 30만원 이상 사용
            elif pre_month >= 300000:
                cal = min(k_pass_price * 0.1, 7000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 신한카드 (체크, 후불, 실물) | K-패스 신한카드 체크 
    def sinhan_check(self, pre_month):
        discount_result = []

        for k_pass_price in self.k_pass :
            # 이전 달, 50만원 이상 사용
            if pre_month >= 500000:
                cal = min(k_pass_price * 0.1, 5000)
            # 이전 달, 20만원 이상 사용
            if pre_month >= 200000:
                cal = min(k_pass_price * 0.1, 2000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 하나카드 (체크, 후불, 실물) | K-패스 하나 체크카드 
    def hana_check(self, pre_month):
        discount_result = []

        for k_pass_price in self.k_pass :
            # 이전 달, 60만원 이상 사용
            if pre_month >= 600000:
                cal = min(k_pass_price * 0.1, 6000)
            # 이전 달, 30만원 이상 사용
            if pre_month >= 300000:
                cal = min(k_pass_price * 0.1, 3000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result
    

    # 하나카드 (신용, 후불, 실물) | K-패스 하나 신용카드
    def hana_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass :
            # 이전 달, 100만원 이상 사용
            if pre_month >= 1000000:
                cal = min(k_pass_price * 0.1, 20000)
            # 이전 달, 50만원 이상 사용
            elif pre_month >= 500000:
                cla = min(k_pass_price * 0.1, 10000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result
    

    # 현대카드 (신용, 후불, 실물) | 현대카드Z work Edition2 
    def handai_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass :
            # 이전 달, 100만원 이상 사용
            if pre_month >= 1000000:
                cal = min(k_pass_price * 0.1, 10000)
            # 이전 달, 50만원 이상 사용
            elif pre_month >= 500000:
                cal = min(k_pass_price * 0.1, 6000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 농협 (체크, 후불, 실물) | K-패스카드(체크) 
    def nonghyup_check(self, pre_month): 
        discount_result = []
        
        for k_pass_price in self.k_pass :
            # 이전 달, 80만원 이상 사용
            if pre_month >= 800000:
                cal = min(k_pass_price * 0.1, 5000)
            # 이전 달, 20만원 이상 사용
            elif pre_month >= 200000:
                cal = min(k_pass_price * 0.1, 3000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 농협 (신용, 후불, 실물) | K-패스카드(신용) 
    def nonghyup_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass :
            # 이전 달, 80만원 이상 사용
            if pre_month >= 800000:
                cal = min(k_pass_price * 0.1, 20000)
            # 이전 달, 40만원 이상 사용
            elif pre_month >= 400000:
                cal = min(k_pass_price * 0.1, 10000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result
    

    # 카카오페이 (선불, 모바일) | 카카오페이 K-패스 모바일 선불교통(안드로이드OS 한정) 
    def kakao_mobile(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass :
            # 이전 달, 30만원 이상 사용
            if pre_month >= 300000:
                cal = min(k_pass_price * 0.1, 7000)
            # 이전 달, 20만원 이상 사용
            elif pre_month >= 200000:
                cal = min(k_pass_price * 0.1, 5000)
            # 이전 달, 10만원 이상 사용
            elif pre_month >= 100000:
                cal = min(k_pass_price * 0.1, 2000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 이동의 즐거움 (선불, 실물 / 모바일) | 이즐 K-패스 카드  
    def ezl_(self, pre_month, subsidiary, young):
        discount_result = []
        
        for k_pass_price in self.k_pass :
            # 이전 달, 30만원 이상 사용
            if pre_month >= 300000:
                # 저소득층
                if subsidiary == "Y":
                    cal = min(k_pass_price * 0.53, 7000)
                # 청년
                elif young == "Y":
                    cal = min(k_pass_price * 0.3, 7000)
                # 일반
                else:
                    cal = min(k_pass_price * 0.2, 7000)

            # 이전 달, 20만원 이상 사용
            elif pre_month >= 200000:
                # 저소득층
                if subsidiary == "Y":
                    cal = min(k_pass_price * 0.53, 5000)
                # 청년
                elif young == "Y":
                    cal = min(k_pass_price * 0.3, 5000)
                # 일반
                else:
                    cal = min(k_pass_price * 0.2, 5000)

            # 이전 달, 10만원 이상 사용
            elif pre_month >= 100000:
                # 저소득층
                if subsidiary == "Y":
                    cal = min(k_pass_price * 0.53, 2000)
                # 청년
                elif young == "Y":
                    cal = min(k_pass_price * 0.3, 2000)
                # 일반
                else:
                    cal = min(k_pass_price * 0.2, 2000)


            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result
    

    # 삼성카드 (신용, 후불, 실물) | K-패스 삼성카드 
    def samsung_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass : 
            # 이전 달, 80만원 이상 사용
            if pre_month >= 800000:
                cal = min(k_pass_price * 0.1, 10000)
            # 이전 달, 40만원 이상 사용
            elif pre_month >= 400000:
                cal = min(k_pass_price * 0.1, 5000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 케이뱅크 (체크, 후불, 실물) | My 체크카드 
    def kbank_check(self, pre_month, pre_trans):
        discount_result = []

        # 이전 달, 30만원 + 대중교통비 5만원 이상 사용
        if pre_month >= 300000 and pre_trans >= 50000:
            discount_result.append(3000)
        else:
            discount_result.append(0)

        return discount_result
    

    # DGB유페이 (선불, 모바일/실물) | 원패스 
    def dgbupay_(self) :
        discount_result = []

        # 혜택 X
        discount_result.append(0)
        return discount_result


    # 기업은행 (신용, 후불, 실물) | K-패스(신용)
    def ibk_credit(self, pre_month):
        discount_result = []

        # 회당 측정
        for cnt in (self.min, self.max) :
            # 이전 달, 50만원 이상 사용
            if pre_month >= 500000 :
                # 일 300원 할인으로 계산
                cal = 10000
            # 이전 달, 20만원 이상 사용
            elif pre_month >= 200000 :
                # 200 * 50 = 10000
                if cnt >= 50 :
                    cal = 10000
                # 200 * 40 = 8000 (예상가격)
                else :
                    cal = 8000
            # 이전 달, 실적 미충족
            else :
                cal = 0
            discount_result.append(cal)

        return discount_result


    # 기업은행 (체크, 후불, 실물) | K-패스(체크)
    def ibk_check(self):
        discount_result = []
        
        # 회당, 100원 할인
        for cnt in (self.min, self.max) :
            cal = min(cnt * 100, 1000)
        discount_result.append(cal)

        return discount_result
    

    # KB국민카드 (신용, 후불, 실물) | K-패스카드 
    def kb_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass : 
            # 이전 달, 30만원 이상 사용
            if pre_month >= 300000:
                cal = min(k_pass_price * 0.1, 5000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # KB국민카드 (체크, 후불, 실물) | K-패스체크카드 
    def kb_check(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass : 
            # 이전 달, 20만원 이상 사용
            if pre_month >= 200000:
                cal = min(k_pass_price * 0.1, 2000)
            # 이전 달, 실적 미충족
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 우리카드 (신용, 후불, 실물) | 우리 K-패스(신용)  
    def woori_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass : 
            # 이전 달, 120만원 이상 사용
            if pre_month >= 1200000:
                cal = min(k_pass_price * 0.1, 40000)
            # 이전 달, 70만원 이상 사용
            elif pre_month >= 700000:
                cal = min(k_pass_price * 0.1, 20000)
            # 이전 달, 30만원 이상 사용
            elif pre_month >= 300000:
                cal = min(k_pass_price * 0.1, 10000)
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result


    # 우리카드 (체크, 후불, 실물) | 우리 K-패스 (COOKIE CHECK) 
    def woori_check(self, pre_trans):
        discount_result = []

        # 대중교통비 5만원 이상 사용
        if pre_trans >= 50000:
            discount_result.append(3000)
        else:
            discount_result.append(0)

        return discount_result


    # 광주은행 (신용, 후불, 실물) | K-그린카드v2  
    def kjbank_credit(self, pre_month):
        discount_result = []
        
        for k_pass_price in self.k_pass : 
            # 이전 달, 30만원 이상 사용
            if pre_month >= 300000:
                cal = min(k_pass_price * 0.1, 3000)
            else:
                cal = 0
            discount_result.append(round(cal))

        return discount_result








## 출력
print(Area.check("경복궁"))    
card = Card()
print("일반 :", Card().original(payment)) 
print("기후동행카드 :", card.gidongca(start_point, end_point, young)) 

# 주거지에 따라 k_pass 값 다르게 출력
if home == "경기" or home == "인천" :
    k_pass = card.k_pass_plus(payment, subsidiary, young)
    print("경기.인천패스 :", card.k_pass_plus(payment, subsidiary, young)) 
else :
    k_pass = card.k_pass(payment, subsidiary, young)
    print("K-패스 :", card.k_pass(payment, subsidiary, young))

discount = Discount(k_pass)
print("<<할인>>")
print("BC 바로카드 (신용, 후불, 실물) :", discount.bc_credit(400000))
print("신한카드 (신용, 후불, 모바일) :", discount.shinhan_credit_tmoney(1000000))
print("신한카드 (신용, 후불, 실물) :", discount.sinhan_credit(1000000))
print("신한카드 (체크, 후불, 실물) :", discount.sinhan_check(1000000))
print("하나카드 (체크, 후불, 실물) :", discount.hana_check(1000000))
print("하나카드 (신용, 후불, 실물) :", discount.hana_credit(1000000))
print("현대카드 (신용, 후불, 실물) :", discount.handai_credit(1000000))
print("농협 (체크, 후불, 실물) :", discount.nonghyup_check(1000000))
print("농협 (신용, 후불, 실물) :", discount.nonghyup_credit(1000000))
print("카카오페이 (선불, 모바일) :", discount.kakao_mobile(1000000))
print("이동의 즐거움 (선불, 실물 / 모바일) :", discount.ezl_(1000000, subsidiary, young))
print("삼성카드 (신용, 후불, 실물) :", discount.samsung_credit(1000000))
print("케이뱅크 (체크, 후불, 실물) :", discount.kbank_check(1000000, 50000))
print("DGB유페이 (선불, 모바x일/실물) :", discount.dgbupay_())
print("기업은행 (신용, 후불, 실물) :", discount.ibk_credit(100000))
print("기업은행 (체크, 후불, 실물) :", discount.ibk_check())
print("KB국민카드 (신용, 후불, 실물) :", discount.kb_credit(1000000))
print("우리카드 (신용, 후불, 실물) :", discount.woori_credit(1000000))
print("우리카드 (체크, 후불, 실물) :", discount.woori_check(1000000))
print("광주은행 (신용, 후불, 실물) :", discount.kjbank_credit(1000000))