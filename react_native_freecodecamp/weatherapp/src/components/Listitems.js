import React from 'react'
import {View,Text,StyleSheet} from 'react-native'
import Feather from 'react-native-vector-icons/Feather'

const ListItem=(props)=>{
    const{dt_txt,min,max,condition}=props
    return(
        <View style={styles.item}>
            <Feather name='sun' size={50} color='#e4a808'/>
            <Text style={styles.date}>{dt_txt}</Text>
            <Text style={styles.tempmin}>{min}</Text>
            <Text style={styles.tempmax}>{max}</Text>
        </View>
    )
}

const styles=StyleSheet.create({
    item:{
        padding:20,
        marginVertical:8,
        marginHorizontal:16,
        flexDirection:'row',
        justifyContent:'space-around',
        borderWidth: 5,
        backgroundColor: '#eed58d'
    },
    tempmax:{
        fontSize:20,
        // color:'#e4a808'
        color:'peru'
    },
    tempmin:{
        fontSize:20,
        color:'#3d3f95'
    },
    date:{
        color:'white',
        fontSize:15
    }
})

export default ListItem