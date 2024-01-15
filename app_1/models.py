# Создайте модель для запоминания бросков монеты: орёл или
# решка.
# Также запоминайте время броска

# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки

from django.db import models


class Coin(models.Model):
    is_heads = models.BooleanField()
    flip_time = models.DateTimeField(auto_now_add=True)


    @staticmethod
    def get_coin_stats(number: int) -> dict:
        last_flips = Coin.objects.all()[:number]
        flips_stats = {
            'heads': [],
            'tails': []
        }
        
        for coin in last_flips:
            if coin.is_heads:
                flips_stats['heads'].append(coin.flip_time)
            else:
                flips_stats['tails'].append(coin.flip_time)
        
        return flips_stats


    def __str__(self):
        return f'Coin flip at {self.flip_time}: heads: {self.is_heads}'
