import React from 'react'
import {View,Text,StyleSheet} from 'react-native'
import Feather from 'react-native-vector-icons/Feather'

const IconText=(props)=>{
    const{iconname,population,color,bodytextstyle}=props
    const{container, texttheme}=styles
    return(
        <View style={container}>
            <Feather name={iconname} size={100} color={color}/>
            <Text style={[texttheme, bodytextstyle]}>{population}</Text>
        </View>
    )
}

const styles=StyleSheet.create({
    texttheme:{
        fontWeight:'bold'
    },
    container:{
        alignItems:'center'
    }
})
export default IconText