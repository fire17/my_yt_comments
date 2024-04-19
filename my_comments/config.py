#config.py

'''
# Open chrome, open developer window, head to Network tab
# (Disable Cache) go to https://myactivity.google.com/page?page=youtube_comments
# Ctrl+F to search for 1PSIDTS
# If results are found, choose "page" cookie, scroll down in the headers until you see the highlighted cookie
# Copy over the entire cookie of these below:

SID = 'YOUR_SID_COOKIE'
HSID = 'YOUR_HSID_COOKIE'
SSID = 'YOUR_SSID_COOKIE'
OSID = 'YOUR_OSID_COOKIE'
__Secure_1PSIDTS = 'YOUR___Secure_1PSIDTS_COOKIE'
'''

cookie='''
HSID=AYSBLLgdMRsBqflM0; SSID=A5bT5BPMpGWCzVTu7; APISID=JYMxxl4tGUkG5VSw/AadLiLwPvGvUkqyTH; SAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-1PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-3PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; ACCOUNT_CHOOSER=AFx_qI7uwo-Zye_loELBKLFeB2iXaP7YSwzsAMl40RbW4CyKDd8u8m9d0wFb53ZsazlnQgmoJGNCoJ6S9svZpiY5Jc2NsPnzoZ4XdNSkh7Gwu3RlsezhDOG02aEDTgvsiXKu0rjZNZ1T; SEARCH_SAMESITE=CgQI3ZgB; SID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4a7kOn_BS-utMrubEKdJq9Q.; __Secure-1PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4DQmscwM_wYSbPGJjvOkpxA.; __Secure-3PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4ffoXeiJRN8dJrnxk7x9pRw.; NID=511=Jy7plyLLidLEmvLD6kjTMAhvR_T6h-PULxMUUbdZhQ1AWdk4wB3u1x3TR5ITJlWis8Eg-NxVXg-hakYRvG_QLp40RdU_L0BcE1a4E4a7BicFn5HGikCBvsL37ChPEMA7PEQ---1ODYJP4MxVnz1dlLT0YzWIzmA06-5kjzcWjvznn9zy0OqsMqd05nRDhULL8zz-hK4_Jgy1FO8ZaIMcmQ6C34B1ONm-7ZBAaXea7u3EhtK84vtPfFN0ULepLTVemCPgFXTET0eEgHLW_M7iwbASSQAr1CLEvl_6upojzXiNOojsvxg6W6X5Q0CFH_uykkD3p5-SnJwXnsgjuk8ImuJr3DDIrYyHJSB0WJyiU_YB; __Host-GAPS=1:rRAi9uVoqZ6Vg7nrCib67DzkgGKxB19OCZekmoxFUK7dc--PDhuz8W8_AALXx8-BXU54oU9kWwHDTD95EgYXn3kEywFDBg:RsM0aRCa743GATWo; LSID=o.calendar.google.com|o.chat.google.com|o.console.cloud.google.com|o.domains.google.com|o.lens.google.com|o.mail.google.com|o.meet.google.com|o.myactivity.google.com|o.photos.fife.usercontent.google.com|o.photos.google.com|o.remotedesktop.google.com|s.IL|s.youtube:bAh-wb9fv84xKAi1g0E3KIPYwVi-BHzXsUPhtoUNtKwsPHwS-7bPTjqpYeDhwd1S5tFIMA.; __Host-1PLSID=o.calendar.google.com|o.chat.google.com|o.console.cloud.google.com|o.domains.google.com|o.lens.google.com|o.mail.google.com|o.meet.google.com|o.myactivity.google.com|o.photos.fife.usercontent.google.com|o.photos.google.com|o.remotedesktop.google.com|s.IL|s.youtube:bAh-wb9fv84xKAi1g0E3KIPYwVi-BHzXsUPhtoUNtKwsPHwSsbwjjbDU2T2FqZSVc5vtAA.; __Host-3PLSID=o.calendar.google.com|o.chat.google.com|o.console.cloud.google.com|o.domains.google.com|o.lens.google.com|o.mail.google.com|o.meet.google.com|o.myactivity.google.com|o.photos.fife.usercontent.google.com|o.photos.google.com|o.remotedesktop.google.com|s.IL|s.youtube:bAh-wb9fv84xKAi1g0E3KIPYwVi-BHzXsUPhtoUNtKwsPHwSNOhH5AKV3pjXkRSOTaFW3w.; __Secure-1PSIDTS=sidts-CjEBSAxbGaexePtSChkgg6UDnAKz9d1wuedturymnpyne2M2CYsiP-vu03oQ15F5BaQuEAA; __Secure-3PSIDTS=sidts-CjEBSAxbGaexePtSChkgg6UDnAKz9d1wuedturymnpyne2M2CYsiP-vu03oQ15F5BaQuEAA; AEC=Ad49MVFb1a7_7duieFGFu4Y7bqOt8bxXtkl8cUlc9FBxg9fLmXVci9E0zQ; 1P_JAR=2023-09-13-08; SIDCC=APoG2W9j7SdvpnhpQx8dv8vYZruGBdiAAj_MutobV0Ve0fYVAIW_ghy_C2rth-P1ihyQt3Y71mcC; __Secure-1PSIDCC=APoG2W89QH88QvvytrvVLYpWczl8osT_-1OCj36aZhm1ifdxPUht44lYrPnsj-NZi8_a_K0JMWCS; __Secure-3PSIDCC=APoG2W8mIavLY-AXi7_YRs1rBb7dlrP837y-5bwLUM-H9h8ho9Bu6gUHF_G_eOuFSKYwFo9GZL0
'''
cookie='''
HSID=AYSBLLgdMRsBqflM0; SSID=A5bT5BPMpGWCzVTu7; APISID=JYMxxl4tGUkG5VSw/AadLiLwPvGvUkqyTH; SAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-1PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-3PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; SEARCH_SAMESITE=CgQI3ZgB; SID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4a7kOn_BS-utMrubEKdJq9Q.; __Secure-1PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4DQmscwM_wYSbPGJjvOkpxA.; __Secure-3PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4ffoXeiJRN8dJrnxk7x9pRw.; NID=511=Jy7plyLLidLEmvLD6kjTMAhvR_T6h-PULxMUUbdZhQ1AWdk4wB3u1x3TR5ITJlWis8Eg-NxVXg-hakYRvG_QLp40RdU_L0BcE1a4E4a7BicFn5HGikCBvsL37ChPEMA7PEQ---1ODYJP4MxVnz1dlLT0YzWIzmA06-5kjzcWjvznn9zy0OqsMqd05nRDhULL8zz-hK4_Jgy1FO8ZaIMcmQ6C34B1ONm-7ZBAaXea7u3EhtK84vtPfFN0ULepLTVemCPgFXTET0eEgHLW_M7iwbASSQAr1CLEvl_6upojzXiNOojsvxg6W6X5Q0CFH_uykkD3p5-SnJwXnsgjuk8ImuJr3DDIrYyHJSB0WJyiU_YB; OSID=bAh-wYqD_ohfIKp6bMAqZ97fUlis4l2TKRRMy4EmtRBiy7ESFASKumOMtmaJT8s8mlhI0A.; __Secure-OSID=bAh-wYqD_ohfIKp6bMAqZ97fUlis4l2TKRRMy4EmtRBiy7ESAwLxk653WNexHRmJYqmoNA.; _ga=GA1.3.1274880982.1694592312; _gid=GA1.3.2103185863.1694592312; OTZ=7204805_44_48_120960_44_365700; AEC=Ad49MVFb1a7_7duieFGFu4Y7bqOt8bxXtkl8cUlc9FBxg9fLmXVci9E0zQ; 1P_JAR=2023-09-13-08; __Secure-1PSIDTS=sidts-CjEBSAxbGavi2HrnxHcwADsFlz465p5-pprDWjVPFd6nBFYk5yfmyvqFLBQqe3BzsiIZEAA; __Secure-3PSIDTS=sidts-CjEBSAxbGavi2HrnxHcwADsFlz465p5-pprDWjVPFd6nBFYk5yfmyvqFLBQqe3BzsiIZEAA; SIDCC=APoG2W9RHrwL7tmeXt7qIQlrty8hyn3YNKe_tBb-m6RYKoFWV_BAweR7o3QRKNW-80C2BIkiALT6; __Secure-1PSIDCC=APoG2W8T7rlhW1MdZ8OnRjFFskqFFTDFTr85IOFRkPf8UPEEGTqnS7tt2PlHk9VghO6id1FbbFqK; __Secure-3PSIDCC=APoG2W-DIc_nAyE6um1YwwcGB7XIKoXPECPPg4dC-wskuBTOXrQlp_PX0Bp24tZ5G6WJNWSxSlQ
'''

cookie='''
HSID=AYSBLLgdMRsBqflM0; SSID=A5bT5BPMpGWCzVTu7; APISID=JYMxxl4tGUkG5VSw/AadLiLwPvGvUkqyTH; SAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-1PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-3PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; SEARCH_SAMESITE=CgQI3ZgB; SID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4a7kOn_BS-utMrubEKdJq9Q.; __Secure-1PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4DQmscwM_wYSbPGJjvOkpxA.; __Secure-3PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4ffoXeiJRN8dJrnxk7x9pRw.; NID=511=Jy7plyLLidLEmvLD6kjTMAhvR_T6h-PULxMUUbdZhQ1AWdk4wB3u1x3TR5ITJlWis8Eg-NxVXg-hakYRvG_QLp40RdU_L0BcE1a4E4a7BicFn5HGikCBvsL37ChPEMA7PEQ---1ODYJP4MxVnz1dlLT0YzWIzmA06-5kjzcWjvznn9zy0OqsMqd05nRDhULL8zz-hK4_Jgy1FO8ZaIMcmQ6C34B1ONm-7ZBAaXea7u3EhtK84vtPfFN0ULepLTVemCPgFXTET0eEgHLW_M7iwbASSQAr1CLEvl_6upojzXiNOojsvxg6W6X5Q0CFH_uykkD3p5-SnJwXnsgjuk8ImuJr3DDIrYyHJSB0WJyiU_YB; OSID=bAh-wYqD_ohfIKp6bMAqZ97fUlis4l2TKRRMy4EmtRBiy7ESFASKumOMtmaJT8s8mlhI0A.; __Secure-OSID=bAh-wYqD_ohfIKp6bMAqZ97fUlis4l2TKRRMy4EmtRBiy7ESAwLxk653WNexHRmJYqmoNA.; _ga=GA1.3.1274880982.1694592312; _gid=GA1.3.2103185863.1694592312; OTZ=7204805_44_48_120960_44_365700; AEC=Ad49MVFb1a7_7duieFGFu4Y7bqOt8bxXtkl8cUlc9FBxg9fLmXVci9E0zQ; 1P_JAR=2023-09-13-08; __Secure-1PSIDTS=sidts-CjEBSAxbGbBk_J0DB_qINKpRSYEZKaiW_DR0i_z42PynjC8oYp4D3jl-9NB8lSHjpAV8EAA; __Secure-3PSIDTS=sidts-CjEBSAxbGbBk_J0DB_qINKpRSYEZKaiW_DR0i_z42PynjC8oYp4D3jl-9NB8lSHjpAV8EAA; SIDCC=APoG2W9u738aOF84EYa0dp6SLYuchdDrBp8rMPjIgAydQEPN_7mLqcTJ8OOfj8ZKtgiAxD-6xMSr; __Secure-1PSIDCC=APoG2W8urRkVyEthYJdfgdsaOabDbDgc5H2ErR1ZU9SD8bYhdSZm9zvmj2URNvIn2SKtF3G0ot1V; __Secure-3PSIDCC=APoG2W84bx295BlyGSU8C_Kpdj5EgCTMYU8ycSQ0dx3Fw32oaZcv_-Zot_BaoVMxOHbd7DD14bU
'''

cookie='''

HSID=AYSBLLgdMRsBqflM0; SSID=A5bT5BPMpGWCzVTu7; APISID=JYMxxl4tGUkG5VSw/AadLiLwPvGvUkqyTH; SAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-1PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; __Secure-3PAPISID=H5WNLYaJusskaoea/A79wxNQlMpSCURlT8; SEARCH_SAMESITE=CgQI3ZgB; SID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4a7kOn_BS-utMrubEKdJq9Q.; __Secure-1PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4DQmscwM_wYSbPGJjvOkpxA.; __Secure-3PSID=awh-wXtv5c6ZlBMMD9p1-rbBZ29Vty0B-vgX1dYsP1JqYEB4ffoXeiJRN8dJrnxk7x9pRw.; OSID=bAh-wYqD_ohfIKp6bMAqZ97fUlis4l2TKRRMy4EmtRBiy7ESFASKumOMtmaJT8s8mlhI0A.; __Secure-OSID=bAh-wYqD_ohfIKp6bMAqZ97fUlis4l2TKRRMy4EmtRBiy7ESAwLxk653WNexHRmJYqmoNA.; _ga=GA1.3.1274880982.1694592312; _gid=GA1.3.2103185863.1694592312; OTZ=7204805_44_48_120960_44_365700; AEC=Ad49MVFb1a7_7duieFGFu4Y7bqOt8bxXtkl8cUlc9FBxg9fLmXVci9E0zQ; NID=511=cEiUYabScSPFtniwg_yCSbnOhVCMjxpO9lZrvUShRiw2-QrZenpxx7FKRffIEn8aLn15bN5dLEIqDO0UuvtMGF4DF-c-VDXUSN8uMR6WAwwy02fEaEKrLq4BlGadxarBMNs2pUOr7LnRsap8v2zxkQMIT1uYAg01kHIOub_L24nQM7pa3lR-tN2FV6FV5NnD183Jv3Rh-sF7HayXFyAtWOGXNsMZLa_FRxRXOkqDEGAj3MP4oVYZhoaKx-cltFYtrm-OLS3dI-N54iTGmXFY8nXl59tE9WWG1PiMOUQJYI_98VbmR92QRpW29raPsfY9RqdXWLFipNcIE_LQPxN2AchfAPjkPF0ps3IiCEGBTx2p; 1P_JAR=2023-09-13-10; __Secure-1PSIDTS=sidts-CjEBSAxbGfGfa7fNTvxMsTEiFtPQYjSB_j8t6SYpkS6D2xpkHUMLIADOnSvZaGqzq-VyEAA; __Secure-3PSIDTS=sidts-CjEBSAxbGfGfa7fNTvxMsTEiFtPQYjSB_j8t6SYpkS6D2xpkHUMLIADOnSvZaGqzq-VyEAA; SIDCC=APoG2W-T-P-uTFEqmkiW_DrSd6TaC0YKkb4NpXBaa-DRY8ggMsvR6RZ0cBuZ8wwsZ9-ex4mJBFA5; __Secure-1PSIDCC=APoG2W-4qbda_Z-_a5ouRz5Zmo4xgz1bIizexbYApgs07LA8H293SXtVpw9LCEBxU6USbYtPaYwy; __Secure-3PSIDCC=APoG2W88IJmLmvRmQes0vT1ivLnGpFOssiFqrXSBAM2xjUhAS0pNDbGsAUdEl662KJLkebjC9Yo'''












cookie_dict = {}
items = cookie.strip("\n").split('; ')
for item in items:
    print("______________")
    print("+++",item)
    key, value, *extra = item.split('=')
    if len(extra)>0:
        value+="="+"=".join(extra)
    print(value)
    cookie_dict[key] = value

print(cookie_dict)

'''

HSID="AYSBLLgdMRsBqflM0"
SSID="A5bT5BPMpGWCzVTu7"
APISID="JYMxxl4tGUkG5VSw/AadLiLwPvGvUkqyTH"
SAPISID="H5WNLYaJusskaoea/A79wxNQlMpSCURlT8"
__Secure_1PAPISID="H5WNLYaJusskaoea/A79wxNQlMpSCURlT8"
__Secure_3PAPISID="H5WNLYaJusskaoea/A79wxNQlMpSCURlT8"
__Secure_1PSIDTS


SID = 'YOUR_SID_COOKIE'
HSID = 'YOUR_HSID_COOKIE'
SSID = 'YOUR_SSID_COOKIE'
OSID = 'YOUR_OSID_COOKIE'
__Secure_1PSIDTS = "sidts-CjEBSAxbGaexePtSChkgg6UDnAKz9d1wuedturymnpyne2M2CYsiP-vu03oQ15F5BaQuEAA"
'''