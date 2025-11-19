# Create PCIDSS Standard Node
standard = """
MERGE (s:Standard {standard_id: 'PCI-DSS'})
ON CREATE SET
    s.standard_name = "Payment Card Industry Security Standards Council",
    s.version = "4.0.1",
    s.publication_date = date("2024-06-11"),
    s.type = "Industry Security Standard",
    s.description = "Global security standard for organizations that handle branded credit cards from major card schemes";

"""

#Create requirements,sub_requirements
pcidss_requirements="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE(r:requirements{standard_id:'PCI-DSS', id:row.id})
ON CREATE SET
    r.parent_id: row.parent_id,
    r.type: row.type,
    r.name: row.name;
"""

#Create Categories
pcidss_categories="""
LOAD CSV WITH HEADERS FROM '$file_path' AS row
MERGE(c:category{standard_id:'PCI-DSS', category_id: row.category_id})
ON CREATE SET
    c:requirement_id: row.requirement_id,
    c:category_name: row.category_name,
    c:objective: row.objective,
    c:counts: row.sub_requirement_count;
"""



        
