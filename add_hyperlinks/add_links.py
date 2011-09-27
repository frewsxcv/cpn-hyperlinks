#!/usr/bin/python

import shapefile


def main():

    sf_old = shapefile.Reader("data/cpn")
    fields_old = sf.fields
    shprec_old = sf.shapeRecords()

    sf_new = shapefile.Writer(shapefile.POINT)

    #newfld = ['LONGITUDE', 'C', 100, 0]
    #fields.append(newfld)
    #newfld = ['LATITUDE', 'C', 100, 0]
    #fields.append(newfld)

    # records
    for rec in shprec_old:
        sf_new.point(*rec.shape.points[0])
        sf_new.record(*rec.record)

    add_fields(fields_old, sf_new)
    add_hyperlinks(shprec_old, fields)

    # Save final shapefile
    sf_new.save("new")


def add_fields(fields, sf):
    '''
    Given a list of fields, copy over the fields to the given shapefile
    '''
    ['HYPERLINK', 'C', 100, 0]
    for fld in fields:
        sf.field(*fld)


def add_hyp_field(fields):
    if hyp_ndx(fields) < 0:
        fields.append(['HYPERLINK', 'C', 100, 0])


def hyp_ndx(fields):
    for i, fld in enumerate(fields):
        try:
            str(fld[0])
        except ValueError:
            continue
        if fld[0] == 'HYPERLINK':
            return i
    return -1


def add_hyperlinks(shprec):
    for rec in shprec:
        (lng, lat) = rec.shape.points[0]
        baseurl = "http://cfslo.no-ip.org/cpn/streetview.cgi"
        hyperlink = baseurl + "?lng=" + str(lng) + "&lat=" + str(lat)
        try:
            rec[hyp_ndx(fields)] = hyperlink
        except IndexError:
            rec.append(hyperlink)
  

main()

## Remove OBJECTID's
#oid_index = fields.index(['OBJECTID', 'N', 9, 0])
#if oid_index:
#    fields.pop(oid_index)
#    for rec in recs:
#        rec.pop(oid_index-1)
