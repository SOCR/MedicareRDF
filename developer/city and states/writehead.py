def write_head(annotationpropertyList, objectpropertyList, classList, fileName): 
    i = 0
    m = 0
    updateFile =  open(fileName,'a')

## head of the RDF/XML file
    updateFile.write('<?xml version="1.0"?>\n')
    updateFile.write('<rdf:RDF xmlns="http://purl.obolirary.org/obo/mebdo/' + fileName +'#"\n')
    updateFile.write('     xml:base="http://purl.obolirary.org/obo/mebdo/' + fileName + '"\n')
    updateFile.write('     xmlns:obo="http://purl.obolibrary.org/obo/"\n     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"\n     xmlns:owl="http://www.w3.org/2002/07/owl#"\n     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"\n     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
    updateFile.write('    <owl:Ontology rdf:about="http://purl.obolirary.org/obo/mebdo/'+ fileName +'"/>\n\n\n')
    
## declare the annotationproperty classes
    if len(annotationpropertyList) > 0 :
        updateFile.write('    <!-- \n    ///////////////////////////////////////////////////////////////////////////////////////\n    //\n    // Annotation Properties\n    //\n    ///////////////////////////////////////////////////////////////////////////////////////\n     -->\n\n')

        m=len(annotationpropertyList)
        for i in range(m):
            annotationProperty = annotationpropertyList[i]
            updateFile.write('    <!-- http://purl.obolibrary.org/obo/'+ annotationProperty+ '  -->\n\n')
            updateFile.write('    <owl:AnnotationProperty rdf:about="http://purl.obolibrary.org/obo/' + annotationProperty + '"/>\n\n\n') 

## declare the objectproperty classes
    if len(objectpropertyList) > 0 :
        updateFile.write('    <!-- \n    ///////////////////////////////////////////////////////////////////////////////////////\n    //\n    // Object Properties\n    //\n    ///////////////////////////////////////////////////////////////////////////////////////\n     -->\n\n')

        m=len(objectpropertyList)
        for i in range(m):
            objectProperty=objectpropertyList[i]
            updateFile.write('    <!-- http://purl.obolibrary.org/obo/'+ objectProperty+ '  -->\n\n')
            updateFile.write('    <owl:ObjectProperty rdf:about="http://purl.obolibrary.org/obo/' + objectProperty + '"/>\n\n\n') 

## declare the classes
    if len(classList) > 0:
        updateFile.write('    <!-- \n    ///////////////////////////////////////////////////////////////////////////////////////\n    //\n    // Classes\n    //\n    ///////////////////////////////////////////////////////////////////////////////////////\n     -->\n\n\n')

        m=len(classList)
        for i in range(m):
            classname=classList[i]
            updateFile.write('    <!-- http://purl.obolibrary.org/obo/' + classname + ' -->\n\n')
            updateFile.write('    <owl:Class rdf:about="http://purl.obolibrary.org/obo/' + classname + '"/>\n\n\n')
    
## individuals 

    updateFile.write('      <!-- \n   ///////////////////////////////////////////////////////////////////////////////////////\n    //\n    // Individuals\n    //\n    ///////////////////////////////////////////////////////////////////////////////////////\n     -->\n\n\n')

    updateFile.write('    <!-- http://dbpedia.org/resource/United_Sates -->\n\n    <owl:NamedIndividual rdf:about="http://dbpedia.org/resource/United_Sates">\n        <rdf:type rdf:resource="http://purl.obolibrary.org/obo/MEBDO_0000020"/>\n        <rdfs:label xml:lang="en">United_States</rdfs:label>\n    </owl:NamedIndividual>\n\n\n')
