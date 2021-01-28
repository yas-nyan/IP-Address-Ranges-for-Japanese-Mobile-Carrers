# IP Address Ranges For Japanese Mobile Carrers

## files
- IPv4: `ipv4_ranges.csv`
- IPv6: `IPv6_ranges.csv`

## sample script
`sample/is_mobile.py`
A simple script for determining the mobile address



## usage
- install

```
git clone https://github.com/yas-nyan/IP-Address-Ranges-for-Japanese-Mobile-Carrers.git
cd IP-Address-Ranges-for-Japanese-Mobile-Carrers/sample
pipenv install  # Or you'll resolve the dependency in some other way.
pipenv run python3 is_mobile.py # Or python3 is_mobile.py
```
- interactive execusion
```
$  python3 is_mobile.py
IP address?: 126.193.0.23
126.193.0.23 is mobile address. (softbank)
IP address?: 240b:c010::111
240b:c010::111 is mobile address. (rakuten)
IP address?: 192.0.2.23
```

## References
(いずれも2021年1月28日閲覧)

### docomo:
- https://www.nttdocomo.co.jp/service/developer/smart_phone/spmode/index.html

### au:
- http://www.au.kddi.com/developer/android/kaihatsu/network/
#### 備考
```
なお、LTE NET for DATA/5G NET for DATAで使用しているグローバルIPアドレスは非公開です。
```
とのこと．



### Softbank: 
- https://www.support.softbankmobile.co.jp/partner/home_tech1/index.cfm

- https://www.support.softbankmobile.co.jp/partner_st/home_tech1/ios/index.cfm

- https://www.support.softbankmobile.co.jp/partner_st/home_tech1/X_series/index.cfm

#### 備考
IPv6の記載が無いため，[総務省資料](https://www.soumu.go.jp/main_content/000517037.pdf)を参照

### Rakuten Mobile

- https://ipinfo.io/AS138384
- https://ipinfo.io/AS23720
- https://ipinfo.io/AS10012

#### 備考
公式HPに記載が無いためRakuten Mobileと名のつくAS(AS138384, AS23720, AS10012) からipinfo.netを利用して検索