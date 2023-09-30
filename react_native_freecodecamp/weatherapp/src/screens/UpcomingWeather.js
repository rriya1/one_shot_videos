import React from 'react'
import { SafeAreaView, StyleSheet,Text, FlatList, View, StatusBar,Image,ImageBackground} from 'react-native'
import Feather from 'react-native-vector-icons/Feather'
import ListItem from '../components/Listitems'

const DATA=[
    {
        dt_txt:'2023-02-18 12:00:00',
        main:{
            temp_max: 8.55,
            temp_min:7.55
        },
        weather:[
            {
                main:'Clear'
            }
        ]
    },
    {
        dt_txt:'2023-02-18 15:00:00',
        main:{
            temp_max: 8.55,
            temp_min:7.55
        },
        weather:[
            {
                main:'Clouds'
            }
        ]
    },
    {
        dt_txt:'2023-02-18 18:00:00',
        main:{
            temp_max: 8.55,
            temp_min:7.55
        },
        weather:[
            {
                main:'Rain'
            }
        ]
    }
]



const UpcomingWeather=()=>{
    const renderItem=({item})=>(
        <ListItem 
        condition={item.weather[0].main} 
        dt_txt={item.dt_txt} 
        min={item.main.temp_min} 
        max={item.main.temp_max}
        />
    )
    return(
        <SafeAreaView style={styles.container}>
            <Text>Upcoming Weather</Text>
            <ImageBackground
            source={require('../../assets/images/upcoming_clouds.jpg')}
            style={styles.image}>
            {/* <Image soource={require('../../assets/images/altocumulus.jpg')} style={styles.image}/> */}
            <FlatList
                data={DATA}
                renderItem={renderItem}
                />
            </ImageBackground>
        </SafeAreaView>
    )
}

const styles=StyleSheet.create({
    container: {
        flex: 1,
        marginTop: StatusBar.currentHeight || 0,
        backgroundColor: '#6474ac'
    },
    image:{
        flex:1
    }
})
export default UpcomingWeather