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
(いずれも2020年閲覧)
docomo:
https://www.nttdocomo.co.jp/service/developer/smart_phone/spmode/index.html


au:
http://www.au.kddi.com/developer/android/kaihatsu/network/


softbank: 
https://www.support.softbankmobile.co.jp/partner/home_tech1/index.cfm

https://www.support.softbankmobile.co.jp/partner_st/home_tech1/ios/index.cfm

https://www.support.softbankmobile.co.jp/partner_st/home_tech1/X_series/index.cf

Rakuten:
TBD
