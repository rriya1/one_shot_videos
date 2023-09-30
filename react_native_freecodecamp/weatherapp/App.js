import React from 'react'
import {View,StyleSheet,Text} from 'react-native'
import CurrentWeather from './src/screens/CurrentWeather'
import UpcomingWeather from './src/screens/UpcomingWeather'
import City from './src/screens/City'
import { NavigationContainer } from 'react-navigation/native'
import  MapmyIndiaGL  from  'mapmyindia-map-react-native-beta';

MapmyIndiaGL.setMapSDKKey("40ab73dbe22826ee1c55cbee8b644c0d");//place your mapsdkKey
MapmyIndiaGL.setRestAPIKey("40ab73dbe22826ee1c55cbee8b644c0d");//your restApiKey
MapmyIndiaGL.setAtlasClientId("33OkryzDZsKEPuxNLD2eHvEyvZ2W6XNCIwYTvc5dWErsN-8XDhrmK2maUHM9q0jY-QQa9Nn1BsvKcgewufu63g==");//your atlasClientId key
MapmyIndiaGL.setAtlasClientSecret("lrFxI-iSEg9TMJc9PIpNkOHsvurtOOXxWZB6FCW-Xmoly3nXnxv_P9QJ0nUdVmSIZOJGbtdC1eFDA4TeTMo1rLboI9qsn9xj"); //your atlasClientSecret key
// MapmyIndiaGL.setAtlasGrantType("");

const App = () =>{

  return (
    <View style={styles.container}>
      {/* <CurrentWeather/>
    </View> */}

    <MapmyIndiaGL.MapView  style={{flex:1}}>
		  <MapmyIndiaGL.Camera
                // ref={c  => (this.camera = c)}
                zoomLevel={12}
                minZoomLevel={4}
                maxZoomLevel={22}
                centerCoordinate={[77.231409,28.6162]}
                 />
		 </MapmyIndiaGL.MapView>
    </View>
    // </View>
  //  </NavigationContainer>
  )

}

const styles= StyleSheet.create({
  container:{
    flex: 1
  }
})

export default App