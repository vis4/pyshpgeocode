# shapegeocode

Usage:

````python
>>> import shapegeocode
>>> gc = shapegeocode.geocoder('NUTS_RG_03M_2006.shp', filter=lambda r: r['STAT_LEVL_'] == 2)
>>> gc.geocode(52.1, 11.7)
{'Shape_Area': '2.68982946020e+000', 'OBJECTID': 271, 'AREA': '0.00000000000e+000', 'LEN': '0.00000000000e+000', 'STAT_LEVL_': 2, 'NUTS_ID': 'DEE0', 'Shape_Leng': '1.30317086814e+001'}
```
