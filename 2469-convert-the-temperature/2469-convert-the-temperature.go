func convertTemperature(celsius float64) []float64 {
    var result []float64
    
    result = append(result, celsius + 273.15)
    result = append(result, celsius * 1.80 + 32.00)

    return result
}