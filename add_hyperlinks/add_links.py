#!/usr/bin/python

import shapefile


def main():
    old_sf = shapefile.Reader("data/cpn")
    old_fields = old_sf.fields
    old_shprec = old_sf.shapeRecords()
    new_sf = shapefile.Writer(shapefile.POINT)

    # fields
    copy_fields(old_fields, new_sf)

    # records
    for old_rec in old_shprec:
        new_sf.point(*old_rec.shape.points[0])
        new_sf.record(*old_rec.record)

    # hyperlinks
    add_hyperlinks(old_shprec, new_sf)

    # save
    new_sf.save("new")


def copy_fields(old_fields, new_sf):
    '''
    Given a list of fields, copy over the fields to the given shapefile
    '''
    hyperlink_field = ('HYPERLINK', 'C', 100, 0)
    for field in old_fields:
        new_sf.field(*field)
    if hyperlink_field not in new_sf.fields:
        new_sf.append(hyperlink_field)


def hyp_index(fields):
    '''
    Returns the HYPERLINK position in a field
    '''
    for i, fld in enumerate(fields):
        if fld[0] == 'HYPERLINK':
            if ('DeletionFlag', 'C', 1, 0) in fields:
                return i-1
            return i


def add_hyperlinks(old_shprec, new_sf):
    '''
    Adds the hyperlinks to the given shapeRecord
    '''
    for rec in old_shprec:
        (lng, lat) = (rec.shape.points[0])
        baseurl = "http://cfslo.no-ip.org/cpn/streetview.cgi"
        hyperlink = baseurl + "?lng=" + str(lng) + "&lat=" + str(lat)
        rec.record[hyp_index(new_sf.fields)] = hyperlink
  

main()

## Remove OBJECTID's
#oid_index = fields.index(['OBJECTID', 'N', 9, 0])
#if oid_index:
#    fields.pop(oid_index)
#    for rec in recs:
#        rec.pop(oid_index-1)
