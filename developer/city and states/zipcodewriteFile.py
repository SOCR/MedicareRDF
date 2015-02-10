def write_zipcode(zipcodeF,cityURI):
    zipcodeF = zipcodeF.strip()
    zipcodeF = str(zipcodeF)
    zipcodeF = (5-len(zipcodeF))* '0'+ zipcodeF
    zipcodeID = '947'+ zipcodeF
    cityURI = str(cityURI)
    updateFile =  open('mebdo_city_county_import.owl','a')
    updateFile.write('    <!-- http://purl.obolibrary.org/obo/MEBDO_'+zipcodeID+' -->\n\n')
    updateFile.write('    <owl:NamedIndividual rdf:about="http://purl.obolibrary.org/obo/MEBDO_'+zipcodeID+'">\n')
    updateFile.write('        <rdf:type rdf:resource="http://purl.obolibrary.org/obo/MEBDO_0000012"/>\n')
    updateFile.write('        <rdfs:label xml:lang="en">'+zipcodeF +' zip code zone</rdfs:label>\n        <rdfs:seeAlso rdf:datatype="http://www.w3.org/2001/XMLSchema#anyURI">http://zipcode.org/'+zipcodeF+'</rdfs:seeAlso>\n    </owl:NamedIndividual>\n\n\n')
    
    updateFile.write('    <!-- ' + str(cityURI) + ' -->\n')
    updateFile.write('    <owl:NamedIndividual rdf:about="'+str(cityURI)+'">\n')
    updateFile.write('        <obo:MEBDO_0000410 rdf:resource="http://purl.obolibrary.org/obo/MEBDO_'+zipcodeID+'"/>\n    </owl:NamedIndividual>\n\n\n')
    
    updateFile.close()