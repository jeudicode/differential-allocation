"""
Differential Allocation-based Genetic Algorithm
"""
import time
import random as rand

class Daga:

    def __init__(self, init_pop = 2, dimensions = 2, min = 0, max = 1, 
    max_cycles = 1, max_pop = 100, lifespan = 10):
        individuals = int(init_pop / 2)

        self.max_cycles = max_cycles

        self.count = 0 # benchmark function calls

        self.males = [
            {
                'genes': [rand.uniform(min,max) for x in range(dimensions)],
                'eval': 0.,
                'fitness': 0
            } for x in range(individuals)]
        self.females = [
            {
                'genes': [rand.uniform(min,max) for x in range(dimensions)],
                'eval': 0.,
                'fitness': 0
            } for x in range(individuals)]
        
        self.children = []
        self.eval_pop()


   
    def selection(self):
        self.taken = []
        for i in self.females:
            partner = rand.randrange(len(self.males))
            if not partner in self.taken:
                self.taken.append(partner)
            else:
                while partner in self.taken:
                    partner = rand.randrange(len(self.males))
                self.taken.append(partner)
            
        
        # print(self.taken)
                
    def crossover(self):
        for i in range(len(self.females)):
            first = {
                'genes': [],
                'eval': 0.,
                'fitness': 0
            }
            second = {
                'genes': [],
                'eval': 0.,
                'fitness': 0
            }

            cross_point = rand.randrange(len(self.females[i]['genes']))

            for j in range(cross_point):
                first['genes'].append(self.females[i]['genes'][j])
                second['genes'].append(self.males[self.taken[i]]['genes'][j])
            for j in range(cross_point, len(self.females[i]['genes'])):
                first['genes'].append(self.males[self.taken[i]]['genes'][j])
                second['genes'].append(self.females[i]['genes'][j])

            first = self.benchmark(first)
            second = self.benchmark(second)

            # self.children.append(first)
            # self.children.append(second)

            if first['eval'] < self.females[i]['eval']:
                self.females[i] = first
            
            if second['eval'] < self.males[self.taken[i]]['eval']:
                self.males[self.taken[i]] = second
        

    def mutation():
        for i in range(len(self.females)):
            rand_fem = rand.randrange(len(self.females))
            rand_male = rand.randrange(len(self.males))
            rand_fem_gene = rand.randrange(len(self.females[rand_fem]['genes']))
            rand_male_gene = rand.randrange(len(self.females[rand_fem]['genes']))
            self.females[rand_fem]['genes'][rand_fem_gene] *= 1 - rand.random()
            self.males[rand_male]['genes'][rand_male_gene] *= 1 - rand.random()

            self.females[rand_fem] = self.benchmark(self.females[rand_fem])
            self.males[rand_male] = self.benchmark(self.males[rand_male])

    def eval_pop(self):
        for i in range(len(self.males)):
            self.males[i] = self.benchmark(self.males[i])
            self.females[i] = self.benchmark(self.females[i])


    def benchmark(self, individual):
        s = 0
        for i in individual['genes']:
            s += i ** 2
        individual['eval'] = s

        self.count += 1

        return individual

        
def main():

    d = Daga(200, 10, -10, 10, 200000, 100, 5)

    while(d.count <= d.max_cycles):
        d.selection()
        d.crossover()
        d.mutation
    #print(d.males)
    #print(d.females)

if __name__ == "__main__":
    main()


