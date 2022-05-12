import http.client
import asyncio, time, datetime

async def refreshTicketDeatils():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nrefreshTicketDeatils \\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('refreshTicketDeatils  : '+ str(len(data)))
    #print(len(data))

async def refreshTicketAttachement():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nrefreshTicketAttachement\\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('refreshTicketAttachement : '+ str(len(data)))
    #print(len(data))
    #return len(data)
    #print(data.decode("utf-8"))

async def refreshExecutedDate():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nrefreshExecutedDate\\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('refreshExecutedDate : '+ str(len(data)))

async def updateClassicClosedDates():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nupdateClassicClosedDates\\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('updateClassicClosedDates : '+ str(len(data)))

async def updateClaasicExecutedDates():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nupdateClaasicExecutedDates\\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('updateClaasicExecutedDates : '+ str(len(data)))

async def refreshSynopsysData():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nrefreshSynopsysData\\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('refreshSynopsysData : '+ str(len(data)))

async def refreshCadenceData():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nrefreshCadenceData\\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('refreshCadenceData : '+ str(len(data)))

async def refreshSiemensData():
    conn = http.client.HTTPSConnection("vendor-audit-service.apps1-fm-int.icloud.intel.com")

    payload = "{\"query\":\"query Query{\\nrefreshSiemensData\\n \\n}\",\"operationName\":\"Query\"}"
    headers = { 'Content-Type': "application/json" }
    conn.request("POST", "/graphql", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print('refreshSiemensData : '+ str(len(data)))

async def main():
    await refreshTicketDeatils()
    await refreshTicketAttachement()
    await refreshExecutedDate()
    await updateClassicClosedDates()
    await updateClaasicExecutedDates()

    await refreshSynopsysData()
    await refreshCadenceData()
    await refreshSiemensData()
    #return result

asyncio.run(main())