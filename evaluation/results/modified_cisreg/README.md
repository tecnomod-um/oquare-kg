# Modifications of cisregEA knowledge graphs

The following modifications have been performed in the [cisreg](https://github.com/juan-mulero/cisregEA) knowledge graphs in order to evaluate the practical performance of the defined metrics.



|                                         |               |           |**Modifications**|       |                 |
|-----------------------------------------|---------------|--------------|----------|-----------|-----------------|
| **Graph name**                          | **Labels**  |**Descriptions**|**Language**|**Datatypes**|**Wrong datatypes**|
| (graph)_d20labels                       | delete 20%    |              |          |           |                 |
| (graph)_d20descriptions                 |               | delete 20%   |          |           |                 |
| (graph)_a90language                     |               |              | add 90%  |           |                 |
| (graph)_a90datatypes                    |               |              |          | add 90%   |                 |
| (graph)_a10wrongDT                      |               |              |          |           | add 10%         |
| (graph)_d20labdesc_a90langDT_a10wrongDT | delete 20%    | delete 20%   | add 90%  | add 90%   | add 10%         |
| (graph)_d50labels                       | delete 50%    |              |          |           |                 |
| (graph)_d50descriptions                 |               | delete 50%   |          |           |                 |
| (graph)_a50language                     |               |              | add 50%  |           |                 |
| (graph)_a50datatypes                    |               |              |          | add 50%   |                 |
| (graph)_a30wrongDT                      |               |              |          |           | add 30%         |
| (graph)_d50labdesc_a50langDT_a30wrongDT | delete 50%    | delete 50%   | add 50%  | add 50%   | add 30%         |
| (graph)_d90labels                       | delete 90%    |              |          |           |                 |
| (graph)_d90descriptions                 |               | delete 90%   |          |           |                 |
| (graph)_a20language                     |               |              | add 20%  |           |                 |
| (graph)_a20datatypes                    |               |              |          | add 20%   |                 |
| (graph)_a50wrongDT                      |               |              |          |           | add 50%         |
| (graph)_d90labdesc_a20langDT_a50wrongDT | delete 90%    | delete 90%   | add 20%  | add 20%   | add 50%         |
| (graph)_d90labdesc_a90langDT_a50wrongDT | delete 90%    | delete 90%   | add 90%  | add 90%   | add 50%         |
| (graph)_a90wrongDT                      |               |              |          |           | add 90%         |
| (graph)_d50labdesc_a50langDT_a90wrongDT | delete 50%    | delete 50%   | add 50%  | add 50%   | add 90%         |
| (graph)_a90DT_a90wrongDT                |               |              |          | add 90%   | add 90%         |
| (graph)_d40labdesc                      | delete 40%    | delete 40%   |          |           |                 |
| (graph)_d40labdesc_a50wrongDT           | delete 40%    | delete 40%   |          |           | add 50%         |

*Table1. Modifications performed in the cisreg knowledge graphs. The column labelled 'Graph name' shows all the knowledge graphs obtained as a result and its modifications.*