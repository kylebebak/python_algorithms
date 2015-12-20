"""
encode(48.669, -4.32913, 24)
encode_base_64(48.669, -4.32913, 24)
"""

from . import url_safe

def _interleave(lat, lon):
    """Interleaves a lat and lon array."""
    lat_lon = []
    for c in range(len(lon)):
        lat_lon.append(lat[c])
        lat_lon.append(lon[c])
    return lat_lon

def _encode(coord, max_coord, precision, encoding=[]):
    coord += max_coord
    for p in range(precision):
        if coord >= max_coord:
            coord -= max_coord
            encoding.append('1')
        else:
            encoding.append('0')
        max_coord /= 2
    return ''.join(encoding)

def encode(lat, lon, precision):
    """Encodes and latitude and longitude as a string of 0s and 1s."""
    lat_hash = _encode(lat, 90, precision)
    lon_hash = _encode(lon, 180, precision)
    geohash = []
    for c in range(len(lon_hash)):
        geohash.append(lat_hash[c])
        geohash.append(lon_hash[c])
    return ''.join(_interleave(lat_hash, lon_hash))

def to_base_64(geohash):
    """Converts binary geohash string to url safe base 64 string."""
    return url_safe.to_base_64(int(geohash, 2))

def encode_base_64(lat, lon, chars):
    return to_base_64(encode(lat, lon, chars*3))


def _neighbor_prev(GH):
    for i in range(len(GH)-1, -1, -1):
        if GH[i] == '0':
            GH[i] = '1'
        else:
            GH[i] = '0'
            break
    return GH

def _neighbor_next(GH):
    for i in range(len(GH)-1, -1, -1):
        if GH[i] == '1':
            GH[i] = '0'
        else:
            GH[i] = '1'
            break
    return GH

def neighbors(geohash):
    lat, lon = [], []
    for i, c in enumerate(geohash):
        lat.append(c) if i%2 == 0 else lon.append(c)
    N = _neighbor_prev(lat)
    W = _neighbor_prev(lon)
    S = _neighbor_next(lat)
    E = _neighbor_next(lon)





