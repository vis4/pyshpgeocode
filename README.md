# pyshpgeocode – merging data and geography

This Python package is for reverse geocoding of data points to shapefile regions. It is developed primarily for assigning administrative region codes to a set of geo coordinates (in standard latitude/longitude). All you need is a shapefile of the regions you want to geocode to.

Usage example:

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

You can speed up the reverse geocoding by limiting the number of polygons that need to be tested. This can be achieved by injecting a ``filter`` function either to the ``geocoder`` constructor or per each ``geocode`` call . 

```python 
# consider only polygons that have STAT_LEVL_ == 2
gc = shapegeocode.geocoder('NUTS_RG_03M_2006.shp', filter=lambda r: r['STAT_LEVL_'] == 2)

# skip every polygon whose NUTS_ID does not begin with "DE"
gc.geocode(53.425, 14.55, filter=lambda r: r['NUTS_ID'][:2] == 'DE')
```

In some situations the lat,lon positions you're dealing with may not be as accurate as your boundary data. For instance, the geo coordinates of coastal cities are often located outside the boundary polygon they belong to. Therefor, you can set the maximum distance (in km) that is still accepted using the ``max_dist`` argument.  

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
