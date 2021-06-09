score = @score

@score = 0

def shifoumi
  puts "Que choisis-tu entre pierre, feuille et ciseaux ?"
 
  player_choice = gets.chomp.downcase
  
  if player_choice == "pierre" || player_choice == "feuille" || player_choice == "ciseaux"
    puts player_choice
  else 
    puts "Le choix n'est pas validé. Choisis entre pierre, feuille et ciseaux :)"
  end

  computer_choice = ["pierre", "feuille", "ciseaux"].sample
  puts computer_choice 
  
  if player_choice == computer_choice
    puts "Pas de bol, égalité !"
    @score = @score
  elsif (player_choice == "feuille" && computer_choice == "ciseaux") ||
        (player_choice == "ciseaux" && computer_choice == "pierre") ||
        (player_choice == "pierre" && computer_choice == "feuille")
    puts "Tu as perdu contre l'ordinateur !"
    if @score > 0
      @score -= 1
    else @score <= 0
      @score
    end
  elsif (player_choice == "feuille" && computer_choice == "pierre") ||
        (player_choice == "ciseaux" && computer_choice == "feuille") ||
        (player_choice == "pierre" && computer_choice == "ciseaux")
    puts "Bravo, t'es un.e winner !"
    @score += 1
  end
  puts @score
end

until @score == 2 do
  shifoumi
end