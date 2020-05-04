import pygeoip
gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr('52.2.150.28')
for key, val in res.items():
    print( key,val)