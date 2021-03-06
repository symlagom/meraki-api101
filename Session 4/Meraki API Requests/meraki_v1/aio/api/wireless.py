class AsyncWireless:
    def __init__(self, session):
        super().__init__()
        self._session = session

    async def getDeviceWirelessBluetoothSettings(self, serial: str):
        """
        **Return the bluetooth settings for a wireless device**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-device-wireless-bluetooth-settings
        
        - serial (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'getDeviceWirelessBluetoothSettings',
        }
        resource = f'/devices/{serial}/wireless/bluetooth/settings'

        return await self._session.get(metadata, resource)

    async def updateDeviceWirelessBluetoothSettings(self, serial: str, **kwargs):
        """
        **Update the bluetooth settings for a wireless device**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-device-wireless-bluetooth-settings
        
        - serial (string)
        - uuid (string): Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        - major (integer): Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        - minor (integer): Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'updateDeviceWirelessBluetoothSettings',
        }
        resource = f'/devices/{serial}/wireless/bluetooth/settings'

        body_params = ['uuid', 'major', 'minor']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getDeviceWirelessConnectionStats(self, serial: str, **kwargs):
        """
        **Aggregated connectivity info for a given AP on this network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-device-wireless-connection-stats
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'connectionStats'],
            'operation': 'getDeviceWirelessConnectionStats',
        }
        resource = f'/devices/{serial}/wireless/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceWirelessLatencyStats(self, serial: str, **kwargs):
        """
        **Aggregated latency info for a given AP on this network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-device-wireless-latency-stats
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'latencyStats'],
            'operation': 'getDeviceWirelessLatencyStats',
        }
        resource = f'/devices/{serial}/wireless/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceWirelessRadioSettings(self, serial: str):
        """
        **Return the radio settings of a device**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-device-wireless-radio-settings
        
        - serial (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'radio', 'settings'],
            'operation': 'getDeviceWirelessRadioSettings',
        }
        resource = f'/devices/{serial}/wireless/radio/settings'

        return await self._session.get(metadata, resource)

    async def updateDeviceWirelessRadioSettings(self, serial: str, **kwargs):
        """
        **Update the radio settings of a device**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-device-wireless-radio-settings
        
        - serial (string)
        - rfProfileId (integer):     The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile
    (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides
    on the device (channel width, channel, power).

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'radio', 'settings'],
            'operation': 'updateDeviceWirelessRadioSettings',
        }
        resource = f'/devices/{serial}/wireless/radio/settings'

        body_params = ['rfProfileId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getDeviceWirelessStatus(self, serial: str):
        """
        **Return the SSID statuses of an access point**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-device-wireless-status
        
        - serial (string)
        """

        metadata = {
            'tags': ['wireless', 'monitor', 'status'],
            'operation': 'getDeviceWirelessStatus',
        }
        resource = f'/devices/{serial}/wireless/status'

        return await self._session.get(metadata, resource)

    async def getNetworkWirelessAirMarshal(self, networkId: str, **kwargs):
        """
        **List Air Marshal scan results from a network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-air-marshal
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'airMarshal'],
            'operation': 'getNetworkWirelessAirMarshal',
        }
        resource = f'/networks/{networkId}/wireless/airMarshal'

        query_params = ['t0', 'timespan']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessBluetoothSettings(self, networkId: str):
        """
        **Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-bluetooth-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'getNetworkWirelessBluetoothSettings',
        }
        resource = f'/networks/{networkId}/wireless/bluetooth/settings'

        return await self._session.get(metadata, resource)

    async def updateNetworkWirelessBluetoothSettings(self, networkId: str, **kwargs):
        """
        **Update the Bluetooth settings for a network. See the docs page for <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a>.**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-bluetooth-settings
        
        - networkId (string)
        - scanningEnabled (boolean): Whether APs will scan for Bluetooth enabled clients. (true, false)
        - advertisingEnabled (boolean): Whether APs will advertise beacons. (true, false)
        - uuid (string): The UUID to be used in the beacon identifier.
        - majorMinorAssignmentMode (string): The way major and minor number should be assigned to nodes in the network. ('Unique', 'Non-unique')
        - major (integer): The major number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
        - minor (integer): The minor number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
        """

        kwargs.update(locals())

        if 'majorMinorAssignmentMode' in kwargs:
            options = ['Unique', 'Non-unique']
            assert kwargs['majorMinorAssignmentMode'] in options, f'''"majorMinorAssignmentMode" cannot be "{kwargs['majorMinorAssignmentMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'updateNetworkWirelessBluetoothSettings',
        }
        resource = f'/networks/{networkId}/wireless/bluetooth/settings'

        body_params = ['scanningEnabled', 'advertisingEnabled', 'uuid', 'majorMinorAssignmentMode', 'major', 'minor']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkWirelessClientsConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by clients**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-clients-connection-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'connectionStats'],
            'operation': 'getNetworkWirelessClientsConnectionStats',
        }
        resource = f'/networks/{networkId}/wireless/clients/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessClientsLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by clients**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-clients-latency-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'latencyStats'],
            'operation': 'getNetworkWirelessClientsLatencyStats',
        }
        resource = f'/networks/{networkId}/wireless/clients/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessClientConnectionStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-client-connection-stats
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'connectionStats'],
            'operation': 'getNetworkWirelessClientConnectionStats',
        }
        resource = f'/networks/{networkId}/wireless/clients/{clientId}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessClientLatencyHistory(self, networkId: str, clientId: str, **kwargs):
        """
        **Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-client-latency-history
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'latencyHistory'],
            'operation': 'getNetworkWirelessClientLatencyHistory',
        }
        resource = f'/networks/{networkId}/wireless/clients/{clientId}/latencyHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessClientLatencyStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated latency info for a given client on this network. Clients are identified by their MAC.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-client-latency-stats
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'latencyStats'],
            'operation': 'getNetworkWirelessClientLatencyStats',
        }
        resource = f'/networks/{networkId}/wireless/clients/{clientId}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-connection-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'connectionStats'],
            'operation': 'getNetworkWirelessConnectionStats',
        }
        resource = f'/networks/{networkId}/wireless/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessDevicesConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by node**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-devices-connection-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'connectionStats'],
            'operation': 'getNetworkWirelessDevicesConnectionStats',
        }
        resource = f'/networks/{networkId}/wireless/devices/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessDevicesLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by node**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-devices-latency-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'latencyStats'],
            'operation': 'getNetworkWirelessDevicesLatencyStats',
        }
        resource = f'/networks/{networkId}/wireless/devices/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessFailedConnections(self, networkId: str, **kwargs):
        """
        **List of all failed client connection events on this network in a given time range**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-failed-connections
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - serial (string): Filter by AP
        - clientId (string): Filter by client MAC
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'failedConnections'],
            'operation': 'getNetworkWirelessFailedConnections',
        }
        resource = f'/networks/{networkId}/wireless/failedConnections'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'serial', 'clientId']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-latency-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'latencyStats'],
            'operation': 'getNetworkWirelessLatencyStats',
        }
        resource = f'/networks/{networkId}/wireless/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkWirelessMeshStatuses(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List wireless mesh statuses for repeaters**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-mesh-statuses
        
        - networkId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'meshStatuses'],
            'operation': 'getNetworkWirelessMeshStatuses',
        }
        resource = f'/networks/{networkId}/wireless/meshStatuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkWirelessRfProfiles(self, networkId: str, **kwargs):
        """
        **List the non-basic RF profiles for this network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-rf-profiles
        
        - networkId (string)
        - includeTemplateProfiles (boolean):     If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template
    should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'getNetworkWirelessRfProfiles',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles'

        query_params = ['includeTemplateProfiles']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def createNetworkWirelessRfProfile(self, networkId: str, name: str, bandSelectionType: str, **kwargs):
        """
        **Creates new RF profile for this network**
        https://developer.cisco.com/docs/meraki-api-v1/#!create-network-wireless-rf-profile
        
        - networkId (string)
        - name (string): The name of the new profile. Must be unique. This param is required on creation.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'. This param is required on creation.
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false. Defaults to true.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ssid', 'ap']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'createNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles'

        body_params = ['name', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def updateNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str, **kwargs):
        """
        **Updates specified RF profile for this network**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-rf-profile
        
        - networkId (string)
        - rfProfileId (string)
        - name (string): The name of the new profile. Must be unique.
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ssid', 'ap']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'updateNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        body_params = ['name', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Delete a RF Profile**
        https://developer.cisco.com/docs/meraki-api-v1/#!delete-network-wireless-rf-profile
        
        - networkId (string)
        - rfProfileId (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'deleteNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        return await self._session.delete(metadata, resource)

    async def getNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Return a RF profile**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-rf-profile
        
        - networkId (string)
        - rfProfileId (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'getNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        return await self._session.get(metadata, resource)

    async def getNetworkWirelessSettings(self, networkId: str):
        """
        **Return the wireless settings for a network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'settings'],
            'operation': 'getNetworkWirelessSettings',
        }
        resource = f'/networks/{networkId}/wireless/settings'

        return await self._session.get(metadata, resource)

    async def updateNetworkWirelessSettings(self, networkId: str, **kwargs):
        """
        **Update the wireless settings for a network**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-settings
        
        - networkId (string)
        - meshingEnabled (boolean): Toggle for enabling or disabling meshing in a network
        - ipv6BridgeEnabled (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
        - locationAnalyticsEnabled (boolean): Toggle for enabling or disabling location analytics for your network
        - ledLightsOn (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'settings'],
            'operation': 'updateNetworkWirelessSettings',
        }
        resource = f'/networks/{networkId}/wireless/settings'

        body_params = ['meshingEnabled', 'ipv6BridgeEnabled', 'locationAnalyticsEnabled', 'ledLightsOn']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkWirelessSsids(self, networkId: str):
        """
        **List the SSIDs in a network. Supports networks with access points or wireless-enabled security appliances and teleworker gateways.**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-ssids
        
        - networkId (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids'],
            'operation': 'getNetworkWirelessSsids',
        }
        resource = f'/networks/{networkId}/wireless/ssids'

        return await self._session.get(metadata, resource)

    async def getNetworkWirelessSsid(self, networkId: str, number: str):
        """
        **Return a single SSID**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-ssid
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids'],
            'operation': 'getNetworkWirelessSsid',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}'

        return await self._session.get(metadata, resource)

    async def updateNetworkWirelessSsid(self, networkId: str, number: str, **kwargs):
        """
        **Update the attributes of an SSID**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-ssid
        
        - networkId (string)
        - number (string)
        - name (string): The name of the SSID
        - enabled (boolean): Whether or not the SSID is enabled
        - authMode (string): The association control method for the SSID ('open', 'psk', 'open-with-radius', '8021x-meraki', '8021x-radius', 'ipsk-with-radius' or 'ipsk-without-radius')
        - enterpriseAdminAccess (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
        - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
        - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
        - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only')
        - splashPage (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth' or 'Sponsored guest'). This attribute is not supported for template children.
        - radiusServers (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusCoaEnabled (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
        - radiusFailoverPolicy (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
        - radiusLoadBalancingPolicy (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
        - radiusAccountingEnabled (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusAccountingServers (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
        - radiusAttributeForGroupPolicies (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
        - ipAssignmentMode (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Layer 3 roaming with a concentrator' or 'VPN')
        - useVlanTagging (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - concentratorNetworkId (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
        - vlanId (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
        - defaultVlanId (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - apTagsAndVlanIds (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - walledGardenEnabled (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
        - walledGardenRanges (array): Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']). Meraki's splash page is automatically included in your walled garden.
        - radiusOverride (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
        - minBitrate (number): The minimum bitrate in Mbps. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
        - bandSelection (string): The client-serving radio frequencies. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
        - perClientBandwidthLimitUp (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
        - perClientBandwidthLimitDown (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
        - lanIsolationEnabled (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
        - visible (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
        - availableOnAllAps (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
        - availabilityTags (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
        """

        kwargs.update(locals())

        if 'authMode' in kwargs:
            options = ['open', 'psk', 'open-with-radius', '8021x-meraki', '8021x-radius', 'ipsk-with-radius', 'ipsk-without-radius']
            assert kwargs['authMode'] in options, f'''"authMode" cannot be "{kwargs['authMode']}", & must be set to one of: {options}'''
        if 'enterpriseAdminAccess' in kwargs:
            options = ['access disabled', 'access enabled']
            assert kwargs['enterpriseAdminAccess'] in options, f'''"enterpriseAdminAccess" cannot be "{kwargs['enterpriseAdminAccess']}", & must be set to one of: {options}'''
        if 'encryptionMode' in kwargs:
            options = ['wep', 'wpa']
            assert kwargs['encryptionMode'] in options, f'''"encryptionMode" cannot be "{kwargs['encryptionMode']}", & must be set to one of: {options}'''
        if 'wpaEncryptionMode' in kwargs:
            options = ['WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only']
            assert kwargs['wpaEncryptionMode'] in options, f'''"wpaEncryptionMode" cannot be "{kwargs['wpaEncryptionMode']}", & must be set to one of: {options}'''
        if 'splashPage' in kwargs:
            options = ['None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest']
            assert kwargs['splashPage'] in options, f'''"splashPage" cannot be "{kwargs['splashPage']}", & must be set to one of: {options}'''
        if 'radiusFailoverPolicy' in kwargs:
            options = ['Deny access', 'Allow access']
            assert kwargs['radiusFailoverPolicy'] in options, f'''"radiusFailoverPolicy" cannot be "{kwargs['radiusFailoverPolicy']}", & must be set to one of: {options}'''
        if 'radiusLoadBalancingPolicy' in kwargs:
            options = ['Strict priority order', 'Round robin']
            assert kwargs['radiusLoadBalancingPolicy'] in options, f'''"radiusLoadBalancingPolicy" cannot be "{kwargs['radiusLoadBalancingPolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'ssids'],
            'operation': 'updateNetworkWirelessSsid',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}'

        body_params = ['name', 'enabled', 'authMode', 'enterpriseAdminAccess', 'encryptionMode', 'psk', 'wpaEncryptionMode', 'splashPage', 'radiusServers', 'radiusCoaEnabled', 'radiusFailoverPolicy', 'radiusLoadBalancingPolicy', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusAttributeForGroupPolicies', 'ipAssignmentMode', 'useVlanTagging', 'concentratorNetworkId', 'vlanId', 'defaultVlanId', 'apTagsAndVlanIds', 'walledGardenEnabled', 'walledGardenRanges', 'radiusOverride', 'minBitrate', 'bandSelection', 'perClientBandwidthLimitUp', 'perClientBandwidthLimitDown', 'lanIsolationEnabled', 'visible', 'availableOnAllAps', 'availabilityTags']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkWirelessSsidFirewallL3FirewallRules(self, networkId: str, number: str):
        """
        **Return the L3 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l3FirewallRules'],
            'operation': 'getNetworkWirelessSsidFirewallL3FirewallRules',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules'

        return await self._session.get(metadata, resource)

    async def updateNetworkWirelessSsidFirewallL3FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L3 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules
        
        - networkId (string)
        - number (string)
        - rules (array): An ordered array of the firewall rules for this SSID (not including the local LAN access rule or the default rule)
        - allowLanAccess (boolean): Allow wireless client access to local LAN (boolean value - true allows access and false denies access) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l3FirewallRules'],
            'operation': 'updateNetworkWirelessSsidFirewallL3FirewallRules',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules'

        body_params = ['rules', 'allowLanAccess']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkWirelessSsidFirewallL7FirewallRules(self, networkId: str, number: str):
        """
        **Return the L7 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l7FirewallRules'],
            'operation': 'getNetworkWirelessSsidFirewallL7FirewallRules',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules'

        return await self._session.get(metadata, resource)

    async def updateNetworkWirelessSsidFirewallL7FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L7 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules
        
        - networkId (string)
        - number (string)
        - rules (array): An array of L7 firewall rules for this SSID. Rules will get applied in the same order user has specified in request. Empty array will clear the L7 firewall rule configuration.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l7FirewallRules'],
            'operation': 'updateNetworkWirelessSsidFirewallL7FirewallRules',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkWirelessSsidSplashSettings(self, networkId: str, number: str):
        """
        **Display the splash page settings for the given SSID**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-ssid-splash-settings
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'splash', 'settings'],
            'operation': 'getNetworkWirelessSsidSplashSettings',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/splash/settings'

        return await self._session.get(metadata, resource)

    async def updateNetworkWirelessSsidSplashSettings(self, networkId: str, number: str, **kwargs):
        """
        **Modify the splash page settings for the given SSID**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-ssid-splash-settings
        
        - networkId (string)
        - number (string)
        - splashUrl (string): [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
        - useSplashUrl (boolean): [optional] Boolean indicating whether the user will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'splash', 'settings'],
            'operation': 'updateNetworkWirelessSsidSplashSettings',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/splash/settings'

        body_params = ['splashUrl', 'useSplashUrl']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def updateNetworkWirelessSsidTrafficShapingRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the traffic shaping settings for an SSID on an MR network**
        https://developer.cisco.com/docs/meraki-api-v1/#!update-network-wireless-ssid-traffic-shaping-rules
        
        - networkId (string)
        - number (string)
        - trafficShapingEnabled (boolean): Whether traffic shaping rules are applied to clients on your SSID.
        - defaultRulesEnabled (boolean):     Whether default traffic shaping rules are enabled (true) or disabled (false).
    There are 4 default rules, which can
    be seen on your network's traffic shaping page. Note that default rules
    count against the rule limit of 8.

        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'trafficShaping', 'rules'],
            'operation': 'updateNetworkWirelessSsidTrafficShapingRules',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules'

        body_params = ['trafficShapingEnabled', 'defaultRulesEnabled', 'rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkWirelessSsidTrafficShapingRules(self, networkId: str, number: str):
        """
        **Display the traffic shaping settings for a SSID on an MR network**
        https://developer.cisco.com/docs/meraki-api-v1/#!get-network-wireless-ssid-traffic-shaping-rules
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'trafficShaping', 'rules'],
            'operation': 'getNetworkWirelessSsidTrafficShapingRules',
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules'

        return await self._session.get(metadata, resource)

