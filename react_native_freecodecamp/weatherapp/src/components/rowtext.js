import React from 'react'
import {View,Text,StyleSheet} from 'react-native'

const Rowtext=(props)=>{
    const{text1,text2,stylefortext1,stylefortext2}=props
    return(
        <View>
            <Text style={stylefortext1}>{text1}</Text>
            <Text style={stylefortext2}>{text2}</Text>
        </View>
    )
}


export default Rowtext