# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ripaparo <ripaparo@student.42madrid.fr>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/28 17:25:31 by ripaparo          #+#    #+#              #
#    Updated: 2025/11/28 17:41:58 by ripaparo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	days = input("Days since last watering: ");

	days = int(days);
	if (days < 2):
		print("Plants are fine")
	else:
		print("Plant is ready to harvest!")