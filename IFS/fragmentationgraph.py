"""Function to generate the fragmentation graph of a given parent cluster."""


def FragmentationGraph(
    parent_ion=[[2, 2, 3], ["Ch", "U", "Cl"], -1, 0], n=3, charges=[1, 0, -1]
):
    """
    Function to generate the fragmentation graph of a given parent cluster.

    Parameters
    ---------
    parent_ion : [number_of_fundamental_moieties, fundamental_moieties,charge,level]
        the list defining the characteristics of the parent ion. default : [[2,2,3],['Ch','U','Cl'],-1,0]

    n : int
        number of fundamental moieties. default : 3

    charges: list of integers
        list of charges of fundamental moieties. default : [1,0,-1]

    Returns
    -------
    daughter_ions : list of all daughter ions given in the prescribed format.

    levels : Depth of the fragmentation tree
    """
    if sum([x * y for x, y in zip(parent_ion[0], charges)]) != parent_ion[2]:
        raise ValueError(
            " Either parent ion list structure or the charges list not accurate"
        )
    levels = 0
    [number_of_moieties, fundamental_moieties, total_charge, levels] = parent_ion
    global daughter_ions
    daughter_ions = []
    seen = set()
    # For the first level of daugther ions produced from parent ion
    for i in range(0, n):
        d_number_of_moieties = number_of_moieties[:]
        d_number_of_moieties[i] = d_number_of_moieties[i] - 1
        daughter_ions.append(
            [
                [number_of_moieties],
                d_number_of_moieties,
                fundamental_moieties,
                sum([x * y for x, y in zip(d_number_of_moieties, charges)]),
                levels + 1,
            ]
        )
        del d_number_of_moieties
    levels = levels + 1
    break_out_flag = False
    while break_out_flag == False:
        for item in daughter_ions:
            if item[4] == levels:
                for j in range(0, n):
                    d_number_of_moieties = item[1][:]
                    d_number_of_moieties[j] = d_number_of_moieties[j] - 1
                    if all(numbers_d >= 0 for numbers_d in d_number_of_moieties):
                        k = tuple(d_number_of_moieties)
                        if k not in seen:
                            seen.add(k)
                            daughter_ions.append(
                                [
                                    [item[1][:]],
                                    d_number_of_moieties,
                                    fundamental_moieties,
                                    sum(
                                        [
                                            x * y
                                            for x, y in zip(
                                                d_number_of_moieties, charges
                                            )
                                        ]
                                    ),
                                    levels + 1,
                                ]
                            )
                        else:
                            for index, value in enumerate(daughter_ions):
                                if value[1][:] == d_number_of_moieties:
                                    daughter_ions[index][0].append(item[1][:])
                    if all(numbers_d <= 0 for numbers_d in d_number_of_moieties):
                        break_out_flag = True
                    del d_number_of_moieties
        levels = levels + 1
    print(
        "Daughter ions (cluster combinations) from this parent ion are: ",
        *daughter_ions,
        sep="\n",
    )
    print("Total number of ions (cluster combinations): " + str(len(daughter_ions)))
    print("Number of levels in the Fragmentation Graph : " + str(levels))
    return daughter_ions, levels


if __name__ == "__main__":
    FragmentationGraph()
