const romanNumeralValues = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000
}

const substractive = {
  I: ['V', 'X'],
  X: ['L', 'C'],
  C: ['D', 'M']
}

/**
 * @param {string} str
 * @returns {number}
 */
function charToInt (str) {
  return romanNumeralValues[str] || -1
}

const noFourRepeatRegex = /I{4,}|V{4,}|X{4,}|C{4,}|D{4,}|L{4,}/
const validCharactersRegex = /[IVXCDLM]/

function checkNotMoreThan3 (romanNumeral) {
  if (romanNumeral.match(noFourRepeatRegex)) {
    throw new Error('romanNumeral must not contain more than 3 times the same roman numeral (except for M)')
  }
}

function checkValid (romanNumeral) {
  if (!romanNumeral.match(validCharactersRegex) || romanNumeral === '') {
    throw new Error('romanNumeral must not be empty and contains only [I, V, X,C, D, L, M]')
  }
  // ne doit pas contenir plus de 3 fois le même chiffre romain sauf pour les milliers (M)
  checkNotMoreThan3(romanNumeral)
}

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
const toNumeric = (romanNumeral) => {
  checkValid(romanNumeral)

  let sum = 0
  const romanNumerals = romanNumeral.split('')
  for (const [i, currentRomanNumeral] of romanNumerals.entries()) {
    const nextRomanNumeral = romanNumeral[i + 1]
    if (i < romanNumerals.length - 1) {
      if (charToInt(currentRomanNumeral) < charToInt(nextRomanNumeral)) {
        const subs = substractive[currentRomanNumeral]
        if (subs && subs.includes(nextRomanNumeral)) {
          sum -= charToInt(currentRomanNumeral)
        } else {
          throw new Error(`Invalid roman numeral: ${romanNumeral}`)
        }
      } else {
        sum += charToInt(currentRomanNumeral)
      }
    } else {
      sum += charToInt(currentRomanNumeral)
    }
  }
  return sum
}

module.exports = {
  toNumeric
}
