# shapegeocode

Usage:

````python
>>> import shapegeocode
>>> gc = shapegeocode.geocoder('NUTS_RG_03M_2006.shp')
>>> gc.geocode(52.1, 11.7)
{
	'NUTS_ID': 'DEE0', 
	'OBJECTID': 271, 
	'STAT_LEVL_': 2
}
```

### Bag of tricks

**Polygon filtering**

You can speed up the geocoding by limiting the number of polygons that should be tested. This can be done either globally or per ``geocode`` call by injecting a ``filter`` function. 

```python
# global filter: 
# consider only polygons that have STAT_LEVL_ == 2
gc = shapegeocode.geocoder('NUTS_RG_03M_2006.shp', filter=lambda r: r['STAT_LEVL_'] == 2)

# local filter:
# skip every polygon whose NUTS_ID does not begin with "DE"
gc.geocode(53.425, 14.55, filter=lambda r: r['NUTS_ID'][:2] == 'DE')
```

**Fuzzy matching**

In some situations the lat,lon positions you're dealing with may not be as accurate as your boundary data. For instance, the geo coordinates of coastal cities are often located outside the boundary polygon they belong to. 

For those situations you can set the maximum distance (in km) that is still accepted using the ``max_dist`` argument.  

```python
>>> gc = shapegeocode.geocoder('NUTS_RG_03M_2006.shp', filter=lambda r: r['NUTS_ID'][:2] == 'DE')
>>> gc.geocode(53.425, 14.55)
None
>>> gc.geocode(53.425, 14.55, max_dist=5)
None
>>> gc.geocode(53.425, 14.55, max_dist=15)
{
	'NUTS_ID': 'DE80',
	'OBJECTID': 185, 
	'STAT_LEVL_': 2
}
```