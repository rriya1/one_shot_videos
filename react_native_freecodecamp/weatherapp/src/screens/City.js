import React from 'react'
import {View,Text,SafeAreaView,StyleSheet,ImageBackground, StatusBar} from 'react-native'
import Feather from 'react-native-vector-icons/Feather'
import IconText from '../../src/components/iconstext'

const City=()=>{
    return(
        <SafeAreaView style={styles.container}>
            <ImageBackground source={require('../../assets/images/city.jpg')} style={styles.imagelayout}>
                <Text>City</Text>
                <Text style={[styles.cityname,styles.citytext]}>London</Text>
                <Text style={[styles.countryname, styles.citytext]}>UK</Text>
                <View style={styles.populationwrapper}>
                   <IconText iconname={'user'} color={'yellow'} population={'1000'} bodytextstyle={styles.populationtext}/> 
                </View>
                <View style={styles.sunrisesetwrap}>
                    <IconText iconname={'sunrise'} color={'white'} population={'6:00:00'} bodytextstyle={styles.sunrise}/> 
                    <IconText iconname={'sunset'} color={'white'} population={'17:34:54'} bodytextstyle={styles.sunset}/> 
                </View>
            </ImageBackground>
        </SafeAreaView>
    )
}

const styles=StyleSheet.create(
    {
        container:{
            flex:1
        },
        imagelayout:
        {
            flex:1
        },
        cityname:{
            fontSize:40
        },
        countryname:{
            fontSize:30

        },

        citytext:{
            fontWeight:'bold',
            color:'white',
            justifyContent:'center',
            alignSelf:'center'
        },

        populationwrapper:{
            flexDirection:'row',
            alignItems:'center',
            justifyContent:'center',
            marginTop:30
        },

        populationtext:{
            fontSize:25,
            marginLeft:7.5,
            color:'white'
        },

        sunrisesetwrap:{
            flexDirection:'row',
            alignItems:'center',
            justifyContent:'space-around',
            marginTop:50 
        },

        sunrise:{
            fontSize:15,
            color:'white'
        },
        sunset:{
            fontSize:15,
            color:'white'
        }
    }
)
export default City