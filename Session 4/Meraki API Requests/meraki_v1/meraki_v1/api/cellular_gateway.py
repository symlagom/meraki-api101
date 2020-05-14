class CellularGateway(object):
    def __init__(self, session):
        super(CellularGateway, self).__init__()
        self._session = session

    def getDeviceCellularGatewaySettings(self, serial: str):
        """
        **Show the LAN Settings of a MG**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-device-cellular-gateway-settings
        
        - serial (string)
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings'],
            'operation': 'getDeviceCellularGatewaySettings',
        }
        resource = f'/devices/{serial}/cellularGateway/settings'

        return self._session.get(metadata, resource)

    def updateDeviceCellularGatewaySettings(self, serial: str, **kwargs):
        """
        **Update the LAN Settings for a single MG.**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-device-cellular-gateway-settings
        
        - serial (string)
        - reservedIpRanges (array): list of all reserved IP ranges for a single MG
        - fixedIpAssignments (array): list of all fixed IP assignments for a single MG
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings'],
            'operation': 'updateDeviceCellularGatewaySettings',
        }
        resource = f'/devices/{serial}/cellularGateway/settings'

        body_params = ['reservedIpRanges', 'fixedIpAssignments']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getDeviceCellularGatewaySettingsPortForwardingRules(self, serial: str):
        """
        **Returns the port forwarding rules for a single MG.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-device-cellular-gateway-settings-port-forwarding-rules
        
        - serial (string)
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'portForwardingRules'],
            'operation': 'getDeviceCellularGatewaySettingsPortForwardingRules',
        }
        resource = f'/devices/{serial}/cellularGateway/settings/portForwardingRules'

        return self._session.get(metadata, resource)

    def updateDeviceCellularGatewaySettingsPortForwardingRules(self, serial: str, **kwargs):
        """
        **Updates the port forwarding rules for a single MG.**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-device-cellular-gateway-settings-port-forwarding-rules
        
        - serial (string)
        - rules (array): An array of port forwarding params
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'portForwardingRules'],
            'operation': 'updateDeviceCellularGatewaySettingsPortForwardingRules',
        }
        resource = f'/devices/{serial}/cellularGateway/settings/portForwardingRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkCellularGatewayConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MG network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations
        
        - networkId (string)
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'getNetworkCellularGatewayConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewayConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MG network**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations
        
        - networkId (string)
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'updateNetworkCellularGatewayConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations'

        body_params = ['destinations']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkCellularGatewaySettingsDhcp(self, networkId: str):
        """
        **List common DHCP settings of MGs**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-cellular-gateway-settings-dhcp
        
        - networkId (string)
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'dhcp'],
            'operation': 'getNetworkCellularGatewaySettingsDhcp',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/dhcp'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewaySettingsDhcp(self, networkId: str, **kwargs):
        """
        **Update common DHCP settings of MGs**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-cellular-gateway-settings-dhcp
        
        - networkId (string)
        - dhcpLeaseTime (string): DHCP Lease time for all MG of the network. It can be '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
        - dnsNameservers (string): DNS name servers mode for all MG of the network. It can take 4 different values: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
        - dnsCustomNameservers (array): list of fixed IP representing the the DNS Name servers when the mode is 'custom'
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'dhcp'],
            'operation': 'updateNetworkCellularGatewaySettingsDhcp',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/dhcp'

        body_params = ['dhcpLeaseTime', 'dnsNameservers', 'dnsCustomNameservers']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkCellularGatewaySettingsSubnetPool(self, networkId: str):
        """
        **Return the subnet pool and mask configured for MGs in the network.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-cellular-gateway-settings-subnet-pool
        
        - networkId (string)
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'subnetPool'],
            'operation': 'getNetworkCellularGatewaySettingsSubnetPool',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/subnetPool'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewaySettingsSubnetPool(self, networkId: str, **kwargs):
        """
        **Update the subnet pool and mask configuration for MGs in the network.**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-cellular-gateway-settings-subnet-pool
        
        - networkId (string)
        - mask (integer): Mask used for the subnet of all MGs in  this network.
        - cidr (string): CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'subnetPool'],
            'operation': 'updateNetworkCellularGatewaySettingsSubnetPool',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/subnetPool'

        body_params = ['mask', 'cidr']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkCellularGatewaySettingsUplink(self, networkId: str):
        """
        **Returns the uplink settings for your MG network.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-cellular-gateway-settings-uplink
        
        - networkId (string)
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'uplink'],
            'operation': 'getNetworkCellularGatewaySettingsUplink',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/uplink'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewaySettingsUplink(self, networkId: str, **kwargs):
        """
        **Updates the uplink settings for your MG network.**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-cellular-gateway-settings-uplink
        
        - networkId (string)
        - bandwidthLimits (object): The bandwidth settings for the 'cellular' uplink
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'settings', 'uplink'],
            'operation': 'updateNetworkCellularGatewaySettingsUplink',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/uplink'

        body_params = ['bandwidthLimits']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

