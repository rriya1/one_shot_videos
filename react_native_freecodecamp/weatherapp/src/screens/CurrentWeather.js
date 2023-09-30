import React from 'react'
import { View,Text, SafeAreaView, StyleSheet} from 'react-native'
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';
import Rowtext from '../components/rowtext'

const CurrentWeather = () =>{
  const{temp,highlow,garment,weather,feels}=styles
  return (
    <SafeAreaView style={styles.wrapper}>
    <View style={styles.container}>
      <MaterialIcons name='wb-sunny' color='peru' size={150}/>
      <Text style={styles.loaction}>Location</Text>
      {/* <Text style={styles.temp}>6</Text>
      <Text style={styles.feels}>Feels like 5</Text> */}
      <Rowtext text1={'  6   '} text2={'Feels like 5'} stylefortext1={temp} stylefortext2={feels}/>
      <View style={styles.highlowwrapper}>
        {/* <Text style={styles.highlow}>High: 8</Text>
        <Text style={styles.highlow}>Low: 6</Text> */}
        <Rowtext text1={'high:8'} text2={'Low: 6'} stylefortext1={highlow} stylefortext2={highlow}/>
      </View>
    </View>
    <View style={styles.bodydown}>
      {/* <Text style={styles.weather}> This is what the weather is like</Text>
      <Text style={styles.garment}> Preffered garment will be displayed here</Text> */}
      <Rowtext text1={'This is what the weather is like'} text2={'Preffered garment will be displayed here'} stylefortext1={weather} stylefortext2={garment}/>
    </View>
    </SafeAreaView>
  )
}

const styles= StyleSheet.create({
   wrapper:{
    flex: 1
   },

   container:{
    backgroundColor: 'papayawhip',
    flex: 1,
    alignItems: 'center'
   },

   loaction:{
    color:'tan',
    fontSize:30
   },

   temp:{
    color:'peru',
    fontSize: 48,
    justifyContent:'center'
   },

   feels:{
    color:'tan',
    fontSize:30
   },

   highlowwrapper:{
    flexDirection:'row'
   },

   highlow:{
    color:'tan',
    fontSize: 20
   },

   weather:{
    color:'papayawhip',
    fontSize: 25
   },

   garment:{
    color:'papayawhip',
    fontSize: 20
   },

   bodydown:{
    justifyContent:'flex-end',
    alignItems:'flex-start',
    backgroundColor:'tan'
   }

   
})

export default CurrentWeather