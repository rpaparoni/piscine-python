# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ripaparo <ripaparo@student.42madrid.fr>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/28 17:01:06 by ripaparo          #+#    #+#              #
#    Updated: 2025/11/28 17:25:06 by ripaparo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	days = input("Enter plant age in days: ");

	days = int(days);
	if (days >= 60):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")