<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
                       xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd">
    <NamedLayer>
        <Name>Female to Male Enrollment in Secondary School</Name>
        <UserStyle>
            <Name>female to male enrollment in secondary school</Name>
            <Title>Female to Male Enrollement in Secondary School</Title>
            <Abstract>A style demonstrating the enrollment ratio of females to males in secondary school</Abstract>
            <FeatureTypeStyle>
                <Rule>
                    <Name>Less than 70</Name>
                    <ogc:Filter>
                        <ogc:PropertyIsLessThan>
                            <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                            <ogc:Literal>70</ogc:Literal>
                        </ogc:PropertyIsLessThan>
                    </ogc:Filter>
                    <PolygonSymbolizer>
                        <Fill>
                            <CssParameter name="fill">#2a7fff</CssParameter>
                            <CssParameter name="fill-opacity">1</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#777777</CssParameter>
                            <CssParameter name="stroke-width">0.60</CssParameter>
                        </Stroke>
                    </PolygonSymbolizer>
                </Rule>
                <Rule>
                    <Name>70 to 90</Name>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                                <ogc:Literal>70</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThan>
                                <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                                <ogc:Literal>90</ogc:Literal>
                            </ogc:PropertyIsLessThan>
                        </ogc:And>
                    </ogc:Filter>
                    <PolygonSymbolizer>
                        <Fill>
                            <CssParameter name="fill">#aaccff</CssParameter>
                            <CssParameter name="fill-opacity">0.4</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#777777</CssParameter>
                            <CssParameter name="stroke-width">0.50</CssParameter>
                        </Stroke>
                    </PolygonSymbolizer>
                </Rule>
                <Rule>
                    <Name>90 to 110</Name>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                                <ogc:Literal>90</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThan>
                                <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                                <ogc:Literal>110</ogc:Literal>
                            </ogc:PropertyIsLessThan>
                        </ogc:And>
                    </ogc:Filter>
                    <PolygonSymbolizer>
                        <Fill>
                            <CssParameter name="fill">#ffffff</CssParameter>
                            <CssParameter name="fill-opacity">0.20</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#777777</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                        </Stroke>
                    </PolygonSymbolizer>
                </Rule>
                <Rule>
                    <Name>110 to 130</Name>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                                <ogc:Literal>110</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThan>
                                <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                                <ogc:Literal>130</ogc:Literal>
                            </ogc:PropertyIsLessThan>
                        </ogc:And>
                    </ogc:Filter>
                    <PolygonSymbolizer>
                        <Fill>
                            <CssParameter name="fill">#ffaaee</CssParameter>
                            <CssParameter name="fill-opacity">0.40</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#777777</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                        </Stroke>
                    </PolygonSymbolizer>
                </Rule>
                <Rule>
                    <Name>Greater than 130</Name>
                    <ogc:Filter>
                        <ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyName>enrollmen4</ogc:PropertyName>
                            <ogc:Literal>130</ogc:Literal>
                        </ogc:PropertyIsGreaterThanOrEqualTo>
                    </ogc:Filter>
                    <PolygonSymbolizer>
                        <Fill>
                            <CssParameter name="fill">#ff2ad4</CssParameter>
                            <CssParameter name="fill-opacity">0.60</CssParameter>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#777777</CssParameter>
                            <CssParameter name="stroke-width">0.5</CssParameter>
                        </Stroke>
                    </PolygonSymbolizer>
                </Rule>
            </FeatureTypeStyle>
        </UserStyle>
    </NamedLayer>
</StyledLayerDescriptor>