/**
 * Permet de convertir un chiffre romain en nombre.
 * @example
 * toNumeric('II') // 2
 * toNumeric('VIII') // 8
 * toNumeric('IX') // 9
 *
 * @param {string} romanNumeral
 * @returns {Number}
 */
function charToInt(str){
    switch (str){
      case 'I' : 
        return 1
        break
      case 'V' : 
        return 5
        break
      case 'X' : 
        return 10
        break
      case 'L' : 
        return 50
        break
      case 'C' : 
        return 100
        break
      case 'D' : 
        return 500
        break
      case 'M' : 
        return 1000
        break
      default :
        return -1
    }
}

const toNumeric = (romanNumeral) => {
  const pattern = /[IVXCDLM]/
  if (!romanNumeral.match(pattern) || romanNumeral == ''){
    return 'error'
  }

 let sum = 0
  for (let i = 0; i < romanNumeral.length; i++){
    if (romanNumeral[i] != 'M' && romanNumeral[i] == romanNumeral[i+1] && romanNumeral[i] == romanNumeral[i+2] && romanNumeral[i] == romanNumeral[i+3]){
      return 'error'
    }
    if(charToInt(romanNumeral[i]) < charToInt(romanNumeral[i+1])){
      if(romanNumeral[i] == 'I' && romanNumeral[i+1] == 'V' || romanNumeral[i+1] == 'X' ){
        sum += charToInt(romanNumeral[i+1]) - charToInt(romanNumeral[i])
        i++
      }
      if(romanNumeral[i] == 'X' && romanNumeral[i+1] == 'L' || romanNumeral[i+1] == 'C'){
        sum += charToInt(romanNumeral[i+1]) - charToInt(romanNumeral[i])
        i++
      }
      if(romanNumeral[i] == 'C' && romanNumeral[i+1] == 'D' || romanNumeral[i+1] == 'M'){
        sum += charToInt(romanNumeral[i+1]) - charToInt(romanNumeral[i])
        i++
      }
    }
    else if (charToInt(romanNumeral[i]) >= charToInt(romanNumeral[i+1])){
      sum += charToInt(romanNumeral[i])
    }  
  }
  return sum 
}

module.exports = {
  toNumeric
}
