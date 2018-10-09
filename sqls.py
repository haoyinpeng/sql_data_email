# -*- coding:utf-8 -*-


W_RESOURCE = '''select ood.ORGANIZATION_NAME,ood.ORGANIZATION_ID,br.resource_code,br.description,crc.resource_rate,br.disable_date 
                  from apps.BOM_RESOURCES br,
                       apps.CST_RESOURCE_COSTS crc,
                       apps.org_organization_definitions ood 
                 where br.organization_id in (510,530,1030,1090) 
                   and br.organization_id = ood.ORGANIZATION_ID 
                   and br.organization_id = crc.organization_id 
                   and br.resource_id = crc.resource_id 
                   and crc.cost_type_id = 1 
                   and br.resource_code like :resource_code'''

W_PARAMS = {'resource_code':'W%'}

W_TITLE = ['库存组织名称','库存组织ID','委外资源编码','描述','委外资源费率','失效日期']
